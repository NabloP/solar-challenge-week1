import pandas as pd
import numpy as np
from scipy.stats import zscore

OUTLIER_COLUMNS = ['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS', 'WSgust']

def clean_solar_data(df: pd.DataFrame, outlier_cols=OUTLIER_COLUMNS) -> pd.DataFrame:
    """
    Cleans a solar dataset by:
    - Converting columns to numeric
    - Flagging outliers using Z-score
    - Imputing missing values with median
    - Dropping outlier rows
    """
    # 1. Convert all to numeric (in case of stray units like 'W/m²')
    for col in outlier_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # 2. Compute Z-scores on median-filled columns
    for col in outlier_cols:
        col_z = f"{col}_z"
        df[col_z] = zscore(df[col].fillna(df[col].median()))

    # 3. Flag outliers
    df['outlier_flag'] = df[[f"{col}_z" for col in outlier_cols]].apply(
        lambda row: any(np.abs(row) > 3), axis=1
    )

    outliers_flagged = df['outlier_flag'].sum()
    print(f"⚠️ Outliers flagged: {outliers_flagged} rows")

    # 4. Impute missing values in key columns
    for col in outlier_cols:
        df[col] = df[col].fillna(df[col].median())

    # 5. Drop outliers and cleanup
    df_clean = df[~df['outlier_flag']].copy()
    z_cols = [f"{col}_z" for col in outlier_cols]
    df_clean.drop(columns=z_cols + ['outlier_flag'], inplace=True)

    print(f"✅ Cleaned data shape: {df_clean.shape}")
    return df_clean
