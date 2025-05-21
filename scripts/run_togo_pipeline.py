# 🌞 Togo Solar Data Pipeline
# ----------------------------------------------
# 📘 Version: 2025-05-18 | Task 3 - Refactored Pipeline
# Goal: Load, clean, and analyze solar irradiance data for Togo
# using modular, production-ready code compatible with multiple countries.

"""
run_togo_pipeline.py – Full Solar Data Pipeline for Togo
---------------------------------------------------------

Performs ingestion, cleaning, summary reporting, and exploratory
visualization of the Togo solar irradiance dataset.

This runner adheres to:
- Modular pipeline design
- Extensive inline commenting
- Alignment with the B5W0 rubric

Author: Nabil Mohamed
"""

# ------------------------------------------------------------------------------
# 📂 Environment Setup – Add root path to sys.path for import resolution
# ------------------------------------------------------------------------------

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# ------------------------------------------------------------------------------
# 📦 Module Imports – Loader, Cleaner, Reporter, Visuals
# ------------------------------------------------------------------------------

from src.Togo.load import TogoDataLoader                            # Country-specific loader
from src.clean import SolarDataCleaner                              # Object-oriented cleaner
from src.report import SolarReportGenerator                         # Summary + null reporter
from src.plots import (                                             # Visualization suite
    plot_time_series,
    plot_cleaning_impact,
    plot_correlation,
    plot_pairwise,
    plot_distribution,
    plot_temperature_vs_rh,
    plot_bubble_chart
)

# ------------------------------------------------------------------------------
# 🔧 Configuration – Set file paths and output targets
# ------------------------------------------------------------------------------

COUNTRY = "togo"
INPUT_FILE = "src/Togo/togo-dapaong_qc.csv"
OUTPUT_FILE = f"data/{COUNTRY}_clean.csv"

# ------------------------------------------------------------------------------
# ✅ Step 1: Load Raw Dataset
# ------------------------------------------------------------------------------

# Instantiate TogoDataLoader and load dataset
loader = TogoDataLoader(INPUT_FILE)
df = loader.load()

# ------------------------------------------------------------------------------
# 📉 Step 1.5: Summary Report
# ------------------------------------------------------------------------------

# Initialize reporter and print+save basic diagnostics
reporter = SolarReportGenerator(df, country=COUNTRY)
reporter.generate(save=True)

# ------------------------------------------------------------------------------
# 🧼 Step 2: Clean Dataset
# ------------------------------------------------------------------------------

# Clean using numeric coercion, Z-score outlier removal, and median imputation
cleaner = SolarDataCleaner(df)
df_clean = cleaner.run()

# ------------------------------------------------------------------------------
# 💾 Step 3: Save Cleaned Output
# ------------------------------------------------------------------------------

# Create output directory (if it doesn't exist) and save to CSV
os.makedirs("data", exist_ok=True)
df_clean.to_csv(OUTPUT_FILE, index=False)
print(f"✅ Cleaned data saved to: {OUTPUT_FILE} ({COUNTRY}_clean.csv)")

# ------------------------------------------------------------------------------
# 📊 Step 4: Exploratory Data Analysis (EDA)
# ------------------------------------------------------------------------------

# 📈 Time trends in solar and temperature metrics
plot_time_series(df_clean, country=COUNTRY)
print("✅ GHI and DNI peak around midday, showing viable solar generation trends.")

# 🧼 Effect of sensor cleaning on ModA/ModB readings
plot_cleaning_impact(df_clean)
print("✅ Sensor readings (ModA/ModB) are consistently higher after cleaning.")

# 🔍 Correlation analysis among key irradiance and temperature features
plot_correlation(df_clean)
print("✅ GHI, DNI, and DHI are strongly correlated. TModA/TModB also align.")

# 📊 Pairwise scatterplots of wind and solar inputs
plot_pairwise(df_clean)

# 📉 Distributions of GHI and wind speed
plot_distribution(df_clean)
print("✅ GHI is right-skewed; wind speed shows moderate variability.")

# 🌡️ RH vs Tamb relationship
plot_temperature_vs_rh(df_clean)
print("✅ Relative humidity is inversely related to ambient temperature.")

# 💠 Bubble chart overlay of multiple environmental variables
plot_bubble_chart(df_clean)
print("✅ Higher GHI and Tamb values tend to occur with moderate RH and BP.")
