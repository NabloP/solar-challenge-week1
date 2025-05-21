"""
run_compare_pipeline.py
----------------------------------------------------------
Main execution script for the SolarComparisonPipeline class.

This script runs the full cross-country solar irradiance analysis
for Benin, Togo, and Sierra Leone as part of Task 3 in the
B5W0: Solar Data Discovery Challenge (10 Academy).

The pipeline performs:
- Data loading from cleaned CSVs
- Statistical testing (Shapiro–Wilk, Kruskal–Wallis)
- Metric visualization (boxplots, bar charts)
- Summary statistics and missing value reports

All outputs are generated using the object-oriented pipeline
in src/compare_pipeline.py and support decision-making for
MoonLight Energy Solutions.

Author: Nabil Mohamed
Date: 21 May 2025
Challenge: B5W0 – Solar Data Discovery
----------------------------------------------------------
"""

import sys
import os

# Ensure the root directory is in the Python path
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(ROOT)

# ------------------------------------------------------------------------------
# 📦 Imports
# ------------------------------------------------------------------------------
from src.compare_pipeline import SolarComparisonPipeline

# ------------------------------------------------------------------------------
# 🚀 Execute full pipeline
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    print("🚀 Launching Solar Comparison Pipeline...\n")

    # Step 1 – Initialize pipeline with default data path
    pipeline = SolarComparisonPipeline(data_path="data")

    # Step 2 – Run entire analysis flow
    results = pipeline.run_all()

    # Step 3 – Confirm success
    print("\n✅ Pipeline execution complete.")
    print("📊 Summary and missing value tables returned.")
