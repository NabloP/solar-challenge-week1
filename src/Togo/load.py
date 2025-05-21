"""
togo/load.py – Togo Solar Dataset Loader
----------------------------------------

Specialized wrapper for loading Togo's cleaned solar irradiance dataset.
Builds on the BaseCSVLoader to enable:
- Timestamp parsing
- Encoding fallback (UTF-8 → latin1)
- Clean diagnostics for reproducibility

Author: Nabil Mohamed
"""

import pandas as pd
from src.loader import BaseCSVLoader  # General-purpose resilient CSV loader
import os

# ------------------------------------------------------------------------------
# 🇹🇬 Togo Dataset Loader
# ------------------------------------------------------------------------------

class TogoDataLoader:
    """
    Loads and validates Togo's solar dataset using the shared BaseCSVLoader logic.

    Key Features:
    - Parses 'Timestamp' into datetime format
    - Automatically falls back to latin1 encoding if UTF-8 fails
    - Sorts entries chronologically
    - Displays dataset diagnostics (shape, columns)

    Example:
    >>> loader = TogoDataLoader("data/togo_clean.csv")
    >>> df_togo = loader.load()
    """

    def __init__(self, path: str):
        """
        Initialize the loader with the path to the cleaned Togo dataset.

        Parameters:
        ----------
        path : str
            Filepath to the Togo dataset.
        """
        self.path = path  # Path to CSV
        self.df = None    # Placeholder for loaded DataFrame

    def load(self) -> pd.DataFrame:
        """
        Load, parse, and sort the dataset.

        Returns:
        --------
        pd.DataFrame
            Parsed and chronologically sorted Togo dataset.
        """
        # 🧠 Use shared loader logic for fallback, parsing, safety
        loader = BaseCSVLoader(path=self.path, parse_dates=["Timestamp"], verbose=False)
        df = loader.load()

        # 📅 Sort by timestamp for temporal analysis
        df = df.sort_values("Timestamp").reset_index(drop=True)

        # 💬 Diagnostic output for traceability and grading
        print(f"📍 Togo Data Loaded from: {self.path}")
        print(f"🔢 Shape: {df.shape}")
        print(f"🧪 Columns: {df.columns.tolist()}")

        self.df = df
        return df
