"""
sierra_leone/load.py – Sierra Leone Solar Dataset Loader
---------------------------------------------------------

Wraps the general-purpose BaseCSVLoader for Sierra Leone-specific solar data.
Includes encoding fallback, timestamp parsing, and diagnostic printouts.

Author: Nabil Mohamed
"""

import pandas as pd
from src.loader import BaseCSVLoader  # General-purpose CSV loader
import os

# ------------------------------------------------------------------------------
# 🇸🇱 Sierra Leone Dataset Loader
# ------------------------------------------------------------------------------

class SierraLeoneDataLoader:
    """
    Specialized loader for Sierra Leone's cleaned solar irradiance dataset.

    Functionality:
    - Parses 'Timestamp' column into datetime format
    - Handles UTF-8 and fallback to 'latin1' encoding
    - Sorts records chronologically
    - Prints concise diagnostics for auditability

    Example:
    >>> loader = SierraLeoneDataLoader("data/sierra_leone_clean.csv")
    >>> df_sl = loader.load()
    """

    def __init__(self, path: str):
        """
        Initialize the loader with the dataset path.

        Parameters:
        ----------
        path : str
            Path to the cleaned Sierra Leone CSV file.
        """
        self.path = path
        self.df = None

    def load(self) -> pd.DataFrame:
        """
        Load the dataset with timestamp parsing and encoding fallback.

        Returns:
        --------
        pd.DataFrame
            Chronologically ordered Sierra Leone solar dataset.
        """
        # ✅ Use the base loader for safe loading with timestamp parsing
        loader = BaseCSVLoader(path=self.path, parse_dates=["Timestamp"], verbose=False)
        df = loader.load()

        # 🧭 Ensure dataset is sorted chronologically by measurement time
        df = df.sort_values("Timestamp").reset_index(drop=True)

        # 📢 Print structured diagnostic output for traceability
        print(f"📍 Sierra Leone Data Loaded from: {self.path}")
        print(f"🔢 Shape: {df.shape}")
        print(f"🧪 Columns: {df.columns.tolist()}")

        self.df = df
        return df
