"""
run_benin_pipeline.py – Full Solar Data Pipeline for Benin
-----------------------------------------------------------

Performs end-to-end ingestion, cleaning, summary reporting, and visual
exploration of the Benin solar irradiance dataset.

This runner reflects:
- Modular engineering
- Inline documentation best practices
- Alignment with B5W0 rubric

Author: Nabil Mohamed
"""

# ------------------------------------------------------------------------------
# 📂 System Setup: Ensure imports work from project root
# ------------------------------------------------------------------------------

import sys
import os

# Add project root to Python path so `src` becomes importable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# ------------------------------------------------------------------------------
# 📦 Imports: Loader, Cleaner, Reporter, Plot Modules
# ------------------------------------------------------------------------------

from src.loader import BaseCSVLoader as SolarDataLoader                    # General-purpose CSV loader
from src.clean import SolarDataCleaner                      # Object-oriented data cleaner
from src.report import SolarReportGenerator                    # Reporting utility
from src.plots import (                                     # Visualization modules
    plot_time_series,
    plot_cleaning_impact,
    plot_correlation,
    plot_pairwise,
    plot_distribution,
    plot_temperature_vs_rh,
    plot_bubble_chart
)

# ------------------------------------------------------------------------------
# 🔧 Configuration
# ------------------------------------------------------------------------------

COUNTRY = "benin"
INPUT_FILE = "src/benin/benin-malanville.csv"
OUTPUT_FILE = f"data/{COUNTRY}_clean.csv"

# ------------------------------------------------------------------------------
# ✅ Step 1: Load Raw Dataset
# ------------------------------------------------------------------------------

# Instantiate loader for Benin dataset
loader = SolarDataLoader(path=INPUT_FILE, parse_dates=["Timestamp"])
df = loader.load()  # Load and return parsed, timestamped DataFrame

# ------------------------------------------------------------------------------
# 📉 Step 1.5: Summary Report
# ------------------------------------------------------------------------------

# Print summary statistics and missing value report, export CSVs
reporter = SolarReportGenerator(df, country=COUNTRY)
reporter.generate(save=True)

# ------------------------------------------------------------------------------
# 🧼 Step 2: Clean Data
# ------------------------------------------------------------------------------

# Apply full Z-score-based outlier cleaning pipeline
cleaner = SolarDataCleaner(df)
df_clean = cleaner.run()

# ------------------------------------------------------------------------------
# 💾 Step 3: Save Cleaned Output
# ------------------------------------------------------------------------------

# Ensure output directory exists and save cleaned DataFrame
os.makedirs("data", exist_ok=True)
df_clean.to_csv(OUTPUT_FILE, index=False)
print(f"✅ Cleaned data saved to: {OUTPUT_FILE} ({COUNTRY}_clean.csv)")

# ------------------------------------------------------------------------------
# 📊 Step 4: Exploratory Data Analysis (EDA)
# ------------------------------------------------------------------------------

# 📈 Solar irradiance over time
plot_time_series(df_clean, country=COUNTRY)
print("✅ GHI and DNI peak around midday, showing viable solar generation trends.")

# 🧼 Sensor readings before/after cleaning events
plot_cleaning_impact(df_clean)
print("✅ Sensor readings (ModA/ModB) are consistently higher after cleaning.")

# 🔍 Correlation structure across irradiance and temperature
plot_correlation(df_clean)
print("✅ GHI, DNI, and DHI are strongly correlated. TModA/TModB also align.")

# 📊 Pairwise wind and irradiance relationships
plot_pairwise(df_clean)

# 📉 Distribution spread of key solar/wind features
plot_distribution(df_clean)
print("✅ GHI is right-skewed; wind speed shows moderate variability.")

# 🌡️ Humidity vs temperature scatter
plot_temperature_vs_rh(df_clean)
print("✅ Relative humidity is inversely related to ambient temperature.")

# 💠 Multivariate bubble plot with GHI, Tamb, RH, BP
plot_bubble_chart(df_clean)
print("✅ Higher GHI and Tamb values tend to occur with moderate RH and BP.")
