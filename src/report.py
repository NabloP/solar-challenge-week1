# src/report.py

import pandas as pd

def summarize_data(df: pd.DataFrame, country: str = "unknown", save: bool = False, output_dir: str = "reports"):
    """
    Generate summary statistics and missing value report for a dataset.

    Args:
        df (pd.DataFrame): The dataset.
        country (str): Country name for labeling.
        save (bool): Whether to save outputs to CSV.
        output_dir (str): Folder for optional exports.
    """
    print(f"📊 Summary Statistics for {country.title()}")
    summary_stats = df.describe()
    display(summary_stats)

    print(f"\n📉 Missing Value Report for {country.title()}")
    missing = df.isna().sum().to_frame(name='Missing Count')
    missing["Percent Missing"] = (missing["Missing Count"] / len(df)) * 100
    display(missing)

    over_5 = missing[missing["Percent Missing"] > 5]
    if not over_5.empty:
        print("⚠️ Columns with >5% missing values:")
        display(over_5)
    else:
        print("✅ No columns with >5% missing values.")

    if save:
        import os
        os.makedirs(output_dir, exist_ok=True)
        summary_stats.to_csv(f"{output_dir}/{country}_summary_stats.csv")
        missing.to_csv(f"{output_dir}/{country}_missing_report.csv")
        print(f"📝 Reports saved to {output_dir}/")

