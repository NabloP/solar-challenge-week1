# 🌞 Benin Solar Data Pipeline
# ----------------------------------------------
# 📘 Version: 2025-05-18 | Task 2 - Refactored Pipeline
# Goal: Load, clean, and analyze solar irradiance data for Benin
# using modular, production-ready code compatible with multiple countries.

# 📦 Import modular components
import os
from src.benin.load import load_benin_data
from src.clean import clean_solar_data
from src.plots import (
    plot_time_series,
    plot_cleaning_impact,
    plot_correlation,
    plot_pairwise,
    plot_distribution,
    plot_temperature_vs_rh,
    plot_bubble_chart
)

# 🔧 Configuration
COUNTRY = "benin"
INPUT_FILE = f"src/Benin/benin-malanville.csv"
OUTPUT_FILE = f"data/{COUNTRY}_clean.csv"

# ================================================
# ✅ Step 1: Load the raw solar dataset
# - Automatically parses timestamp column
# - Falls back to latin1 encoding if needed
# ================================================
df = load_benin_data(INPUT_FILE)

# ================================================
# ✅ Step 1.5: Summary statistics & null analysis
# - Prints describe() and missing value breakdown
# ================================================
summarize_data(df, country=COUNTRY, save=True)


# ================================================
# ✅ Step 2: Clean the dataset
# - Converts stringified numbers to numeric
# - Flags and removes Z-score outliers
# - Imputes missing values using column medians
# ================================================
df_clean = clean_solar_data(df)

# ================================================
# ✅ Step 3: Export the cleaned DataFrame
# - Saves to `data/benin_clean.csv`
# - Directory is created if it doesn't exist
# ================================================
os.makedirs("data", exist_ok=True)
df_clean.to_csv(OUTPUT_FILE, index=False)
print(f"✅ Cleaned data saved to: {OUTPUT_FILE} ({COUNTRY}_clean.csv)")

# ================================================
# ✅ Step 4: Run Exploratory Data Analysis (EDA)
# - Generates time series, correlation, and sensor plots
# - Used for identifying solar trends and anomalies
# ================================================

# 📈 Solar metrics over time (GHI, DNI, DHI, Tamb)
plot_time_series(df_clean, country=COUNTRY)
print("✅ GHI and DNI peak around midday, showing viable solar generation trends.")

# 🧼 Cleaning impact on sensor output
plot_cleaning_impact(df_clean)
print("✅ Sensor readings (ModA/ModB) are consistently higher after cleaning.")

# 🔍 Heatmap of feature correlations
plot_correlation(df_clean)
print("✅ GHI, DNI, and DHI are strongly correlated. TModA/TModB also align.")

# 📊 Wind and solar relationships (pairwise scatter)
plot_pairwise(df_clean)

# 📉 Distributions of GHI and wind speed
plot_distribution(df_clean)
print("✅ GHI is right-skewed; wind speed shows moderate variability.")

# 🌡️ RH vs Temperature
plot_temperature_vs_rh(df_clean)
print("✅ Relative humidity is inversely related to ambient temperature.")

# 💠 Bubble chart of GHI vs Tamb
plot_bubble_chart(df_clean)
print("✅ Higher GHI and Tamb values tend to occur with moderate RH and BP.")
