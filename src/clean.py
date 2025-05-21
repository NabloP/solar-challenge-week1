"""
clean.py – Solar Data Cleaning Module
-------------------------------------

Encapsulates outlier detection and cleaning logic for solar
radiation datasets using object-oriented design.

Author: Nabil Mohamed
"""

import pandas as pd # import pandas for data manipulation
import numpy as np # import numpy for numerical operations
from scipy.stats import zscore # import zscore for statistical calculations

# ------------------------------------------------------------------------------
# 🧼 SolarDataCleaner Class
# ------------------------------------------------------------------------------
class SolarDataCleaner: # class to clean solar data
    """
    Cleans solar data by:
    - Converting key columns to numeric
    - Flagging outliers using Z-scores
    - Imputing missing values using medians
    - Dropping rows with extreme values
    """

    def __init__(self, df: pd.DataFrame, outlier_columns=None): # constructor to initialize the class
        """
        Initialize cleaner with a dataset and relevant columns.
        """
        default_cols = ['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS', 'WSgust'] # default columns to clean
        self.df = df.copy() # copy the dataframe to avoid modifying the original
        self.outlier_columns = outlier_columns or default_cols # set default columns if none provided
        print(f"🧼 Cleaner initialized with {self.df.shape[0]} rows")

    def convert_to_numeric(self): # method to convert columns to numeric
        """
        Force all target columns to numeric (coerce invalid values to NaN).
        This helps clean up units like 'W/m²' or bad parses.
        """
        for col in self.outlier_columns: # iterate through each column
            self.df[col] = pd.to_numeric(self.df[col], errors='coerce') # convert to numeric
        print("🔢 Converted target columns to numeric")

    def flag_outliers(self): # method to flag outliers
        """
        Compute Z-scores for outlier columns and flag any row with |Z| > 3.
        """
        for col in self.outlier_columns: # iterate through each column
            col_z = f"{col}_z" # create a new column for Z-scores
            self.df[col_z] = zscore(self.df[col].fillna(self.df[col].median())) # calculate Z-scores

        self.df['outlier_flag'] = self.df[ # create a flag for outliers
            [f"{col}_z" for col in self.outlier_columns] # iterate through Z-score columns
        ].apply(lambda row: any(np.abs(row) > 3), axis=1) # check if any Z-score is greater than 3

        flagged = self.df['outlier_flag'].sum() # count flagged rows
        print(f"⚠️ Flagged {flagged} outlier rows") # print the number of flagged rows

    def impute_missing(self): # method to impute missing values
        """
        Fill missing values in all key columns using the column median.
        """
        for col in self.outlier_columns: # iterate through each column
            self.df[col] = self.df[col].fillna(self.df[col].median()) # impute missing values with median
        print("🩹 Missing values imputed (median)")

    def drop_outliers(self) -> pd.DataFrame: # method to drop outliers
        """
        Return a cleaned dataframe with outliers removed and helper columns dropped.
        """
        z_cols = [f"{col}_z" for col in self.outlier_columns] # get Z-score columns
        df_clean = self.df[~self.df['outlier_flag']].copy() # create a copy of the dataframe without outliers
        df_clean.drop(columns=z_cols + ['outlier_flag'], inplace=True) # drop Z-score and flag columns
        print(f"✅ Final cleaned shape: {df_clean.shape}") # print the final shape of the cleaned dataframe
        return df_clean # return the cleaned dataframe

    def run(self) -> pd.DataFrame: # method to run the full cleaning pipeline
        """
        Execute the full cleaning pipeline.
        """
        self.convert_to_numeric() # convert columns to numeric
        self.flag_outliers() # flag outliers
        self.impute_missing() # impute missing values
        return self.drop_outliers() # return the cleaned dataframe
