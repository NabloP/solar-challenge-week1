# Solar Challenge Week 1 - 10 Academy

## 🗂 Challenge Context
This repository is part of the 10 Academy B5W0: Solar Data Discovery challenge. It explores solar radiation and environmental sensor data from Benin, Togo, and Sierra Leone to identify high-potential regions for solar investment. It includes data cleaning, EDA, cross-country analysis, and a Streamlit dashboard for interactive insights.

## 🔧 Project Setup

To reproduce this environment:

1. Clone the repository:
   ```bash
   git clone https://github.com/NabloP/solar-challenge-week1.git
   cd solar-challenge-week1
   ```

2. Create and activate a virtual environment:
   
   **On Windows:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

    **On macOS/Linux:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```

## ⚙️ CI/CD (GitHub Actions)

This project uses GitHub Actions for Continuous Integration. On every push or pull_request event, the following workflow is triggered:

- Checkout repo

- Set up Python 3.10

- Install dependencies from requirements.txt

CI workflow is defined at:

    `.github/workflows/ci.yml`

## 📁 Project Structure

<!-- TREE START -->
📁 Project Structure

solar-challenge-week1/
├── LICENSE
├── README.md
├── project-tree.txt
├── requirements.txt
├── .github/
│   └── workflows/
│       ├── ci.yml
│       ├── unittests.yml
├── data/
│   ├── benin_clean.csv
│   ├── sierra_leone_clean.csv
│   ├── togo_clean.csv
├── notebooks/
│   ├── benin_eda.ipynb
│   ├── sierra_leone_eda.ipynb
│   ├── togo_eda.ipynb
├── reports/
│   ├── benin_missing_report.csv
│   ├── benin_summary_stats.csv
│   ├── sierra_leone_missing_report.csv
│   ├── sierra_leone_summary_stats.csv
│   ├── togo_missing_report.csv
│   ├── togo_summary_stats.csv
├── scripts/
│   ├── README.md
│   ├── __init__.py
│   ├── generate_tree.py
│   ├── run_benin_pipeline.py
│   ├── run_sierra_leone_pipeline.py
│   ├── run_togo_pipeline.py
├── src/
│   ├── clean.py
│   ├── plots.py
│   ├── report.py
│   ├── Benin/
│   │   ├── benin-malanville.csv
│   │   ├── load.py
│   ├── Sierra_Leone/
│   │   ├── load.py
│   │   ├── sierraleone-bumbuna.csv
│   └── Togo/
│       ├── load.py
│       ├── togo-dapaong_qc.csv
└── tests/
    ├── __init__.py
<!-- TREE END -->

## ✅ Status
 ☑︎ GitHub repo initialized

 ☑︎ Virtual environment set up

 ☑︎ CI/CD via GitHub Actions configured

 ☑︎ Project structured and committed

 ☑︎ Exploratory Data Analysis
 + ☑︎ Benin EDA pipeline complete and modularized  complete and modularized  
 + ☑︎ Togo EDA pipeline complete and modularized  
 + ☑︎ Sierra Leone pipeline  complete and modularized  


## 📦 What's in This Repo

This repository documents the Week 1 challenge for 10 Academy’s AI Mastery Bootcamp. It includes:

📁 **Scaffolded directory structure** using best practices for `src/`, `notebooks/`, `scripts/`, and `tests/`

- 🧪 **CI/CD integration** via GitHub Actions for reproducibility and reliability

- 🧹 **README auto-updating** via `scripts/generate_tree.py` to keep documentation aligned with project layout

- 📊 **Modular EDA workflows** for Benin, Sierra Leone, and Togo to clean and compare solar datasets

- 📚 **Clear Git hygiene** (no committed `.venv` or `.csv`), commit messages and pull request usage

- 🧠 **My Contributions:** All project scaffolding, README setup, automation scripts, and CI configuration were done from scratch by me

## 🧪 Usage

###To run the modular Benin pipeline:

```bash
python scripts/run_benin_pipeline.py
```

This script will:

1. Load the raw Benin solar dataset from `src/Benin/benin-malanville.csv`

2. Clean the data (outlier removal, median imputation)

3. Export cleaned data to: `data/benin_clean.csv`

4. Generate summary statistics and missing-value report in: reports/

    - `benin_summary_stats.csv`
    - `benin_missing_report.csv`

5. Produce a full suite of visualizations:

    - Time series plots of GHI, DNI, etc.
    - Sensor cleaning impact
    - Correlation heatmap
    - Wind-solar pair plots
    - Distributions and bubble chart

⚠️ The pipeline is designed to run from the project root. If executing from /notebooks, it will auto-adjust the working directory.

###To run the modular Togo pipeline:

```bash
python scripts/run_togo_pipeline.py
```

This script will:

1. Load the raw Togo solar dataset from `src/Togo/togo-dapaong_qc.csv`

2. Clean the data (outlier removal, median imputation)

3. Export cleaned data to: `data/togo_clean.csv`

4. Generate summary statistics and missing-value report in: reports/

    - `togo_summary_stats.csv`
    - `togo_missing_report.csv`

5. Produce a full suite of visualizations:

    - Time series plots of GHI, DNI, etc.
    - Sensor cleaning impact
    - Correlation heatmap
    - Wind-solar pair plots
    - Distributions and bubble chart

⚠️ The pipeline is designed to run from the project root. If executing from /notebooks, it will auto-adjust the working directory.

###To run the modular Sierra Leone pipeline:

```bash
python scripts/run_sierra_leone_pipeline.py
```

This script will:

1. Load the raw Sierra Leone solar dataset from `src/Sierra_Leone/sierraleone-bumbuna.csv`

2. Clean the data (outlier removal, median imputation)

3. Export cleaned data to: `data/sierra_leone_clean.csv`

4. Generate summary statistics and missing-value report in: reports/

    - `sierra_leone__summary_stats.csv`
    - `sierra_leone_missing_report.csv`

5. Produce a full suite of visualizations:

    - Time series plots of GHI, DNI, etc.
    - Sensor cleaning impact
    - Correlation heatmap
    - Wind-solar pair plots
    - Distributions and bubble chart

⚠️ The pipeline is designed to run from the project root. If executing from /notebooks, it will auto-adjust the working directory.

## 🚀 Author
Nabil Mohamed
AIM Bootcamp Participant
GitHub: [NabloP](https://github.com/NabloP)