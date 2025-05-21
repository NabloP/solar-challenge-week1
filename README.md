# Solar Challenge Week 1 - 10 Academy

## 🗂 Challenge Context
This repository contains the submission for 10 Academy’s B5W0: Solar Data Discovery Challenge. The goal is to evaluate solar irradiance and environmental sensor data across Benin, Togo, and Sierra Leone to identify high-potential regions for solar farm investment.

The project includes:

📊 Data cleaning and preprocessing pipelines

🔬 Exploratory Data Analysis (EDA)

🧠 Modular code using OOP principles

⚙️ CI/CD pipeline

🖥️ Interactive Streamlit dashboard (planned)

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
│   ├── compare_countries.ipynb
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
│   ├── run_compare_pipeline.py
│   ├── run_sierra_leone_pipeline.py
│   ├── run_togo_pipeline.py
├── src/
│   ├── __init__.py
│   ├── clean.py
│   ├── compare_pipeline.py
│   ├── loader.py
│   ├── plots.py
│   ├── report.py
│   ├── Benin/
│   │   ├── __init__.py
│   │   ├── benin-malanville.csv
│   │   ├── load.py
│   ├── Sierra_Leone/
│   │   ├── __init__.py
│   │   ├── load.py
│   │   ├── sierraleone-bumbuna.csv
│   └── Togo/
│       ├── __init__.py
│       ├── load.py
│       ├── togo-dapaong_qc.csv
└── tests/
    ├── __init__.py
<!-- TREE END -->

## ✅ Status
- ☑️ Repository initialized
- ☑️ GitHub Actions CI configured
- ☑️ Modular OOP pipelines for each country
- ☑️ Summary + missing value diagnostics
- ☑️ Full EDA including:
    - Time Series Trends
    - Sensor Cleaning Impact
    - Correlation Heatmap
    - Pairwise Scatter Matrix
    - Distribution Plots
    - Bubble Chart


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

## To run the modular Compare Countries pipeline:

```bash
python scripts/run_compare_pipeline.py
```
This script will:

1. Load the cleaned datasets for Benin, Togo, and Sierra Leone from the data/ directory:
    - `data/benin_clean.csv`
    - `data/togo_clean.csv`
    - `data/sierra_leone_clean.csv`
2. Run statistical analysis:
    - Shapiro–Wilk test on GHI per country (tests for normality)
    - Kruskal–Wallis test comparing GHI distributions (non-parametric ANOVA)
3. Produce cross-country visualizations:
    - Boxplots of GHI, DNI, DHI distributions by country
    - Bar chart comparing average GHI across countries
4. Print consolidated summary statistics and missing-value report:
    - Mean, median, std, and count by metric/country
    - Null counts and percentages grouped by country

⚠️ The pipeline requires that all three cleaned `.csv` files already exist in `data/`. Ensure you've run the Benin, Togo, and Sierra Leone pipelines first. The script is designed to run from the project root and will auto-adjust if launched from a subdirectory.

## 🧠 Design Philosophy
This project was developed with a focus on:

- ✅ Modular Python design using classes, helper modules, and runners
- ✅ High commenting density to meet AI and human readability expectations
- ✅ Reproducibility through consistent Git hygiene and generate_tree.py
- ✅ Rubric alignment with clear insights and analysis pipelines per country

## 🚀 Author
Nabil Mohamed
AIM Bootcamp Participant
GitHub: [NabloP](https://github.com/NabloP)