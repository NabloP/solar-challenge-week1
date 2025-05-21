"""
loader.py – General-Purpose CSV Loader
--------------------------------------

Provides a reusable class for robustly loading CSV files with:
- Timestamp parsing
- Encoding fallback (UTF-8 → latin1)
- Verbose feedback for diagnostics

Intended as a base module for more domain-specific loaders.

Author: Nabil Mohamed
"""

import os  # OS module for file path validation
import pandas as pd  # Pandas for data loading and manipulation

# ------------------------------------------------------------------------------
# 📂 BaseCSVLoader Class
# ------------------------------------------------------------------------------

class BaseCSVLoader:
    """
    A general-purpose loader for CSV files with built-in fault tolerance
    and timestamp parsing.

    Usage:
        loader = BaseCSVLoader("data/my_file.csv", parse_dates=["Timestamp"])
        df = loader.load()

    Parameters:
    ----------
    path : str
        Path to the CSV file on disk.
    parse_dates : list[str], optional
        Columns to parse as datetime objects.
    verbose : bool
        Whether to print diagnostics on load.
    """

    def __init__(self, path: str, parse_dates=None, verbose: bool = True):
        self.path = path  # Store file path
        self.parse_dates = parse_dates if parse_dates else []  # Default: no date parsing
        self.verbose = verbose  # Toggle console output

    def load(self) -> pd.DataFrame:
        """
        Attempt to read the CSV file using UTF-8 encoding first.
        If that fails, retry with 'latin1' fallback.

        Returns:
        --------
        pd.DataFrame
            Loaded DataFrame with optional datetime parsing.
        """

        # Step 1: Confirm file exists
        if not os.path.exists(self.path):
            raise FileNotFoundError(f"❌ File not found: {self.path}")

        # Step 2: Try reading the file with UTF-8 encoding
        try:
            df = pd.read_csv(self.path, parse_dates=self.parse_dates)
            encoding_used = "utf-8"
        except UnicodeDecodeError:
            # Step 3: Retry with Latin-1 fallback on encoding error
            print(f"⚠️ Encoding issue in {self.path}. Retrying with latin1...")
            df = pd.read_csv(self.path, parse_dates=self.parse_dates, encoding="latin1")
            encoding_used = "latin1"

        # Step 4: Print summary diagnostics if verbose mode is on
        if self.verbose:
            print(f"✅ Loaded: {self.path}")
            print(f"🔢 Shape: {df.shape}")
            print(f"🧪 Columns: {df.columns.tolist()}")
            print(f"📦 Encoding Used: {encoding_used}")

        return df  # Return the fully loaded DataFrame
