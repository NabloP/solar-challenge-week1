# src/report.py

import pandas as pd
import os

def summarize_data(df: pd.DataFrame, country: str = "", save: bool = False):
    """Print and optionally export summary statistics and null report."""
    print(f"📊 Summary Statistics for {country.title()}")
    summary_stats = df.describe()
    print(summary_stats)  # ← changed from display()

    print("\n📉 Missing Values:")
    missing = df.isna().sum().to_frame(name="Missing Count")
    missing["Percent Missing"] = (missing["Missing Count"] / len(df)) * 100
    print(missing)  # ← changed from display()

    if save:
        os.makedirs("reports", exist_ok=True)
        summary_stats.to_csv(f"reports/{country}_summary_stats.csv")
        missing.to_csv(f"reports/{country}_missing_report.csv")
        print(f"✅ Reports saved to reports/{country}_*.csv")
