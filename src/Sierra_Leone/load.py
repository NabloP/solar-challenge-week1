import pandas as pd
import os

def read_csv_safe(path):
    """Safely load a CSV file with fallback encoding and timestamp parsing."""
    try:
        return pd.read_csv(path, parse_dates=["Timestamp"])
    except UnicodeDecodeError:
        print(f"⚠️ Encoding issue in {path}. Retrying with latin1...")
        return pd.read_csv(path, parse_dates=["Timestamp"], encoding="latin1")

def load_sierra_leone_data(path: str) -> pd.DataFrame:
    """Load and return Sierra Leone solar data, sorted by Timestamp."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"❌ File not found: {path}")
    
    df = read_csv_safe(path)
    df = df.sort_values("Timestamp").reset_index(drop=True)
    
    print(f"✅ Loaded: {path}")
    print("🔢 Shape:", df.shape)
    print("🧪 Columns:", df.columns.tolist())
    
    return df
