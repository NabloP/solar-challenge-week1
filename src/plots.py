import matplotlib.pyplot as plt
import seaborn as sns

def plot_time_series(df, country):
    """
    📈 Time Series Analysis
    Plots GHI, DNI, DHI, and Tamb over time to examine solar trends and temperature variation.
    Useful to detect seasonal cycles, peak hours, and anomalies in data collection.
    """
    fig, axs = plt.subplots(2, 2, figsize=(14, 8))
    cols = ['GHI', 'DNI', 'DHI', 'Tamb']

    for ax, col in zip(axs.flat, cols):
        ax.plot(df["Timestamp"], df[col])
        ax.set_title(f"{col} over Time for {country.title()}")
        ax.set_xlabel("Timestamp")
        ax.set_ylabel(col)

    plt.tight_layout()
    plt.show()

def plot_cleaning_impact(df):
    """
    🧼 Cleaning Impact Analysis
    Compares average sensor output (ModA and ModB) before and after cleaning events.
    Cleaning = 1 implies maintenance occurred at that time.
    """
    df.groupby("Cleaning")[["ModA", "ModB"]].mean().plot(kind='bar', figsize=(8, 5))
    plt.title("Sensor Readings Before vs After Cleaning")
    plt.xlabel("Cleaning Event (0 = No, 1 = Yes)")
    plt.ylabel("Average Irradiance (W/m²)")
    plt.tight_layout()
    plt.show()

def plot_correlation(df):
    """
    🔍 Correlation Heatmap
    Visualizes relationships between key solar and temperature metrics.
    Helps identify which features are redundant or strongly related (e.g., GHI ~ DNI).
    """
    corr_cols = ['GHI', 'DNI', 'DHI', 'TModA', 'TModB']
    corr = df[corr_cols].corr()

    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap of Solar Metrics")
    plt.tight_layout()
    plt.show()

def plot_pairwise(df):
    """
    📊 Pairwise Scatter Matrix
    Explores relationships between wind features and solar output (GHI).
    Useful for detecting non-linear trends, clusters, or outliers.
    """
    sns.pairplot(df, vars=['WS', 'WSgust', 'WD', 'GHI'], kind='scatter')

def plot_distribution(df):
    """
    📉 Distribution Analysis
    Plots histograms for GHI and Wind Speed to inspect skewness and spread.
    """
    df[['GHI', 'WS']].hist(bins=30, figsize=(10, 4))
    plt.suptitle("Distributions of GHI and Wind Speed")
    plt.tight_layout()
    plt.show()

def plot_temperature_vs_rh(df):
    """
    🌡️ Temperature vs Humidity
    Scatter plot to examine how Relative Humidity correlates with Ambient Temperature.
    Helps detect inverse seasonal relationships or sensor drift.
    """
    sns.scatterplot(data=df, x='RH', y='Tamb')
    plt.title("Relative Humidity vs Ambient Temperature")
    plt.xlabel("Relative Humidity (%)")
    plt.ylabel("Ambient Temperature (°C)")
    plt.tight_layout()
    plt.show()

def plot_bubble_chart(df):
    """
    💠 Bubble Chart: GHI vs Tamb
    - X-axis: Global Horizontal Irradiance
    - Y-axis: Ambient Temperature
    - Size: Relative Humidity
    - Hue: Barometric Pressure

    This plot provides a compact overview of how solar output, temperature, and air conditions interact.
    """
    sns.scatterplot(data=df, x='GHI', y='Tamb', size='RH', hue='BP', alpha=0.6)
    plt.title("Bubble Chart: GHI vs Tamb (size=RH, hue=BP)")
    plt.xlabel("GHI (W/m²)")
    plt.ylabel("Tamb (°C)")
    plt.tight_layout()
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.show()
