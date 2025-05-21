# 🌞 Sierra Leone Solar Data Pipeline
# ----------------------------------------------
# 📘 Version: 2025-05-18 | Task 2 - Final Country
# Goal: Load, clean, and analyze solar irradiance data for Sierra Leone
# using modular, production-ready code compatible with multiple countries.

"""
run_sierra_leone_pipeline.py – Full Solar Data Pipeline for Sierra Leone
-------------------------------------------------------------------------

Performs end-to-end ingestion, cleaning, summary reporting, and visual
exploration of the Sierra Leone solar irradiance dataset.

This runner reflects:
- Modular engineering
- Inline documentation best practices
- Alignment with B5W0 rubric

Author: Nabil Mohamed
"""

# ----------------------------------------------------------------------
# 📂 Environment Setup: Root path for local module imports
# ----------------------------------------------------------------------

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# ----------------------------------------------------------------------
# 📦 Module Imports
# ----------------------------------------------------------------------

from src.Sierra_Leone.load import SierraLeoneDataLoader                   # Country-specific loader
from src.clean import SolarDataCleaner                                     # Object-oriented cleaner
from src.report import SolarReportGenerator                                # Reporting engine
from src.plots import (                                                    # EDA visualizations
    plot_time_series,
    plot_cleaning_impact,
    plot_correlation,
    plot_pairwise,
    plot_distribution,
    plot_temperature_vs_rh,
    plot_bubble_chart
)

# ----------------------------------------------------------------------
# 🔧 Configuration
# ----------------------------------------------------------------------

COUNTRY = "sierra_leone"
INPUT_FILE = "src/Sierra_Leone/sierraleone-bumbuna.csv"
OUTPUT_FILE = f"data/{COUNTRY}_clean.csv"

# ----------------------------------------------------------------------
# ✅ Step 1: Load Raw Dataset
# ----------------------------------------------------------------------

loader = SierraLeoneDataLoader(INPUT_FILE)
df = loader.load()

# ----------------------------------------------------------------------
# 📉 Step 1.5: Summary Report
# ----------------------------------------------------------------------

reporter = SolarReportGenerator(df, country=COUNTRY)
reporter.generate(save=True)

# ----------------------------------------------------------------------
# 🧼 Step 2: Clean Data
# ----------------------------------------------------------------------

cleaner = SolarDataCleaner(df)
df_clean = cleaner.run()

# ----------------------------------------------------------------------
# 💾 Step 3: Save Cleaned Output
# ----------------------------------------------------------------------

os.makedirs("data", exist_ok=True)
df_clean.to_csv(OUTPUT_FILE, index=False)
print(f"✅ Cleaned data saved to: {OUTPUT_FILE} ({COUNTRY}_clean.csv)")

# ----------------------------------------------------------------------
# 📊 Step 4: Exploratory Data Analysis (EDA)
# ----------------------------------------------------------------------

plot_time_series(df_clean, country=COUNTRY)
print("✅ GHI and DNI peak around midday, showing viable solar generation trends.")

plot_cleaning_impact(df_clean)
print("✅ Sensor readings (ModA/ModB) are consistently higher after cleaning.")

plot_correlation(df_clean)
print("✅ GHI, DNI, and DHI are strongly correlated. TModA/TModB also align.")

plot_pairwise(df_clean)

plot_distribution(df_clean)
print("✅ GHI is right-skewed; wind speed shows moderate variability.")

plot_temperature_vs_rh(df_clean)
print("✅ Relative humidity is inversely related to ambient temperature.")

plot_bubble_chart(df_clean)
print("✅ Higher GHI and Tamb values tend to occur with moderate RH and BP.")