"""
benin/load.py – Benin Solar Dataset Loader
------------------------------------------

Wraps the general-purpose BaseCSVLoader for Benin-specific data.
Adds timestamp sorting and diagnostics with clear logging.

Author: Nabil Mohamed
"""

import pandas as pd
from src.loader import BaseCSVLoader  # Reuse the general-purpose CSV loader
import os

# ------------------------------------------------------------------------------
# 🇧🇯 Benin Dataset Loader
# ------------------------------------------------------------------------------

class BeninDataLoader:
    """
    Specialized loader for Benin's cleaned solar irradiance dataset.

    Builds on top of BaseCSVLoader:
    - Handles timestamp parsing
    - Applies encoding fallback if necessary
    - Sorts chronologically
    - Logs key file diagnostics

    Example:
    >>> loader = BeninDataLoader("data/benin_clean.csv")
    >>> df_benin = loader.load()
    """

    def __init__(self, path: str):
        """
        Initialize loader for Benin's dataset.

        Parameters:
        ----------
        path : str
            Path to the cleaned Benin CSV file.
        """
        self.path = path  # Store path for internal reference
        self.df = None    # Placeholder for the loaded DataFrame

    def load(self) -> pd.DataFrame:
        """
        Load the CSV, sort by timestamp, and print diagnostics.

        Returns:
        --------
        pd.DataFrame
            Chronologically ordered Benin solar dataset.
        """
        # ✅ Use shared CSV loader with 'Timestamp' column parsing
        loader = BaseCSVLoader(path=self.path, parse_dates=["Timestamp"], verbose=False)
        df = loader.load()

        # 📊 Sort the dataset chronologically
        df = df.sort_values("Timestamp").reset_index(drop=True)

        # 💬 Diagnostics (customized for Benin loader)
        print(f"📍 Benin Data Loaded from: {self.path}")
        print(f"🔢 Shape: {df.shape}")
        print(f"🧪 Columns: {df.columns.tolist()}")

        # ✅ Assign to self and return
        self.df = df
        return df
