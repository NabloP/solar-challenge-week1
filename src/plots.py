"""
plots.py – Solar Data Visualization Module
------------------------------------------

Contains reusable plotting functions for time series, correlations,
sensor performance, distributions, and environmental relationships
in solar radiation datasets.

All functions are designed for modular integration in notebooks,
scripts, and dashboards.

Author: Nabil Mohamed
"""

import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------------------------------------------
# 📈 1. Time Series Visualization
# ------------------------------------------------------------------------------
def plot_time_series(df, country):
    """
    Plot GHI, DNI, DHI, and Ambient Temperature (Tamb) over time.

    Parameters:
    - df (pd.DataFrame): Cleaned dataframe for one country
    - country (str): Country name for plot titles

    Purpose:
    - Detects seasonal variation, daily cycles, or sensor anomalies
    - Highlights irradiance behavior across different solar components
    """
    fig, axs = plt.subplots(2, 2, figsize=(14, 8))  # 2x2 grid of plots
    cols = ['GHI', 'DNI', 'DHI', 'Tamb']            # Metrics to plot

    for ax, col in zip(axs.flat, cols):  # One plot per column
        ax.plot(df["Timestamp"], df[col])  # Line plot of time series
        ax.set_title(f"{col} over Time for {country.title()}")
        ax.set_xlabel("Timestamp")
        ax.set_ylabel(col)

    plt.tight_layout()
    plt.show()

# ------------------------------------------------------------------------------
# 🧼 2. Sensor Cleaning Impact
# ------------------------------------------------------------------------------
def plot_cleaning_impact(df):
    """
    Compare ModA and ModB sensor output before and after cleaning events.

    Parameters:
    - df (pd.DataFrame): Cleaned dataframe containing 'Cleaning' and ModA/B

    Purpose:
    - Verifies if cleaning had a measurable effect on sensor output
    - Encourages proactive maintenance planning
    """
    df.groupby("Cleaning")[["ModA", "ModB"]].mean().plot(kind='bar', figsize=(8, 5))
    plt.title("Sensor Readings Before vs After Cleaning")
    plt.xlabel("Cleaning Event (0 = No, 1 = Yes)")
    plt.ylabel("Average Irradiance (W/m²)")
    plt.tight_layout()
    plt.show()

# ------------------------------------------------------------------------------
# 🔍 3. Correlation Heatmap
# ------------------------------------------------------------------------------
def plot_correlation(df):
    """
    Visualize correlations between solar irradiance and module temperature.

    Parameters:
    - df (pd.DataFrame): Cleaned dataframe

    Purpose:
    - Identifies multicollinearity among solar inputs
    - Supports feature selection for modeling
    """
    corr_cols = ['GHI', 'DNI', 'DHI', 'TModA', 'TModB']
    corr = df[corr_cols].corr()

    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap of Solar Metrics")
    plt.tight_layout()
    plt.show()

# ------------------------------------------------------------------------------
# 📊 4. Pairwise Scatter Matrix
# ------------------------------------------------------------------------------
def plot_pairwise(df):
    """
    Create scatter matrix for wind and GHI features.

    Parameters:
    - df (pd.DataFrame): Cleaned dataframe

    Purpose:
    - Explore joint distributions and clustering patterns
    - Reveal nonlinear or directional relationships
    """
    sns.pairplot(df, vars=['WS', 'WSgust', 'WD', 'GHI'], kind='scatter')
    plt.suptitle("Pairwise Wind & Irradiance Relationships", y=1.02)
    plt.tight_layout()
    plt.show()

# ------------------------------------------------------------------------------
# 📉 5. Distribution Histograms
# ------------------------------------------------------------------------------
def plot_distribution(df):
    """
    Show histograms of GHI and Wind Speed to assess skewness and range.

    Parameters:
    - df (pd.DataFrame): Cleaned dataframe

    Purpose:
    - Detect outlier ranges or need for normalization
    - Visually confirm distributional assumptions
    """
    df[['GHI', 'WS']].hist(bins=30, figsize=(10, 4))
    plt.suptitle("Distributions of GHI and Wind Speed")
    plt.tight_layout()
    plt.show()

# ------------------------------------------------------------------------------
# 🌡️ 6. Temperature vs Relative Humidity
# ------------------------------------------------------------------------------
def plot_temperature_vs_rh(df):
    """
    Scatter plot showing how RH varies with Tamb.

    Parameters:
    - df (pd.DataFrame): Cleaned dataframe

    Purpose:
    - Examine inverse humidity–temperature effects
    - Spot trends that could affect sensor efficiency
    """
    sns.scatterplot(data=df, x='RH', y='Tamb')
    plt.title("Relative Humidity vs Ambient Temperature")
    plt.xlabel("Relative Humidity (%)")
    plt.ylabel("Ambient Temperature (°C)")
    plt.tight_layout()
    plt.show()

# ------------------------------------------------------------------------------
# 💠 7. Bubble Chart: GHI vs Tamb (RH + BP)
# ------------------------------------------------------------------------------
def plot_bubble_chart(df):
    """
    Multi-dimensional scatter plot visualizing:

    - X-axis: GHI
    - Y-axis: Tamb
    - Size: RH (Relative Humidity)
    - Hue: BP (Barometric Pressure)

    Parameters:
    - df (pd.DataFrame): Cleaned dataframe

    Purpose:
    - Visualize how atmospheric variables jointly impact solar output
    - Highlight clusters or edge-case weather conditions
    """
    sns.scatterplot(
        data=df,
        x='GHI',
        y='Tamb',
        size='RH',
        hue='BP',
        alpha=0.6
    )
    plt.title("Bubble Chart: GHI vs Tamb (size = RH, hue = BP)")
    plt.xlabel("GHI (W/m²)")
    plt.ylabel("Tamb (°C)")
    plt.tight_layout()
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.show()
