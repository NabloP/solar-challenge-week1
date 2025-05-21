"""
reports.py – Summary & Missing Value Reporter
---------------------------------------------

This module encapsulates the logic for printing and exporting
basic data quality reports including summary statistics and
missing value percentages.

Author: Nabil Mohamed
"""

import pandas as pd
import os

# ------------------------------------------------------------------------------
# 📋 SolarReportGenerator Class
# ------------------------------------------------------------------------------
class SolarReportGenerator:
    """
    Generates and optionally exports summary statistics and missing value reports
    for a given solar dataset.

    Usage:
        reporter = SolarReportGenerator(df, country="Benin")
        reporter.generate(save=True)
    """

    def __init__(self, df: pd.DataFrame, country: str = ""):
        """
        Initialize with a cleaned DataFrame and optional country label.

        Parameters:
        - df (pd.DataFrame): Input solar dataset
        - country (str): Optional country label for labeling outputs
        """
        self.df = df
        self.country = country.title()
        print(f"📝 Initialized report generator for {self.country}")

    def get_summary_stats(self) -> pd.DataFrame:
        """
        Compute summary statistics (mean, std, percentiles).

        Returns:
        - pd.DataFrame: Summary stats using describe()
        """
        return self.df.describe()

    def get_missing_report(self) -> pd.DataFrame:
        """
        Compute count and percentage of missing values.

        Returns:
        - pd.DataFrame: Table with missing count and percent
        """
        missing = self.df.isna().sum().to_frame(name="Missing Count")
        missing["Percent Missing"] = (missing["Missing Count"] / len(self.df)) * 100
        return missing

    def generate(self, save: bool = False):
        """
        Generate and optionally save the summary and missing reports.

        Parameters:
        - save (bool): If True, exports reports as CSV files in /reports
        """
        print(f"\n📊 Summary Statistics for {self.country}")
        summary = self.get_summary_stats()
        print(summary)

        print(f"\n📉 Missing Values Report for {self.country}")
        missing = self.get_missing_report()
        print(missing)

        if save:
            os.makedirs("reports", exist_ok=True)
            summary.to_csv(f"reports/{self.country}_summary_stats.csv")
            missing.to_csv(f"reports/{self.country}_missing_report.csv")
            print(f"\n✅ Reports saved to reports/{self.country}_*.csv")
