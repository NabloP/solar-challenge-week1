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
├── notebooks/
├── scripts/
│   ├── README.md
│   ├── __init__.py
│   ├── generate_tree.py
├── src/
│   ├── Benin/
│   │   ├── csps-yls_wapp_stationinstallationreport_benin-malanville_2021-08-08_fr_en.pdf
│   │   ├── csps-yls_wapp_stationinstallationreport_benin-parakou_2021-08-13_fr_en.pdf
│   │   ├── csps-yls_wapp_stationmeasurementreport_benin-malanville_2022-08-09_fr_en.pdf
│   │   ├── csps-yls_wapp_stationmeasurementreport_benin-malanville_2023-08-09-final_fr_en.pdf
│   │   ├── csps-yls_wapp_stationmeasurementreport_benin-parakou_2022-08-12_fr_en.pdf
│   │   ├── csps-yls_wapp_stationmeasurementreport_benin-parakou_2023-08-12-final_fr_en.pdf
│   │   ├── solar-measurements_benin-malanville_header_fr_en.xlsx
│   │   ├── solar-measurements_benin-malanville_qc.csv
│   │   ├── solar-measurements_benin-malanville_qc_year2.csv
│   │   ├── solar-measurements_benin-parakou_header_fr_en.xlsx
│   │   ├── solar-measurements_benin-parakou_qc.csv
│   │   ├── solar-measurements_benin-parakou_qc_year2.csv
│   ├── Sierra Leone/
│   └── Togo/
│       ├── csps-yls_wapp_stationinstallationreport_togo_dapaong_2021-10-24_fr_en.pdf
│       ├── csps-yls_wapp_stationinstallationreport_togo_davie_2021-11-02_fr_en.pdf
│       ├── csps-yls_wapp_stationmeasurementreport_togo-dapaong_2022-10-24_fr_en.pdf
│       ├── csps-yls_wapp_stationmeasurementreport_togo-dapaong_2023-10-24-final_fr_en.pdf
│       ├── csps-yls_wapp_stationmeasurementreport_togo-davie_2022-11-03_fr_en.pdf
│       ├── csps-yls_wapp_stationmeasurementreport_togo-davie_2023-11-03-final_fr_en.pdf
│       ├── solar-measurements_togo-dapaong_header_fr_en.xlsx
│       ├── solar-measurements_togo-dapaong_qc.csv
│       ├── solar-measurements_togo-dapaong_qc_year2.csv
│       ├── solar-measurements_togo-davie_header_fr_en.xlsx
│       ├── solar-measurements_togo-davie_qc.csv
│       ├── solar-measurements_togo-davie_qc_year2.csv
└── tests/
    ├── __init__.py
<!-- TREE END -->

## ✅ Status
 ☑︎ GitHub repo initialized

 ☑︎ Virtual environment set up

 ☑︎ CI/CD via GitHub Actions configured

 ☑︎ Project structured and committed

 ☐ Exploratory Data Analysis (in progress...)


## 📦 What's in This Repo

This repository documents the Week 1 challenge for 10 Academy’s AI Mastery Bootcamp. It includes:

📁 **Scaffolded directory structure** using best practices for `src/`, `notebooks/`, `scripts/`, and `tests/`

- 🧪 **CI/CD integration** via GitHub Actions for reproducibility and reliability

- 🧹 **README auto-updating** via `scripts/generate_tree.py` to keep documentation aligned with project layout

- 📊 **Planned EDA workflows** for Benin, Sierra Leone, and Togo to clean and compare solar datasets

- 📚 **Clear Git hygiene** (no committed `.venv` or `.csv`), commit messages and pull request usage

- 🧠 **My Contributions:** All project scaffolding, README setup, automation scripts, and CI configuration were done from scratch by me

## 🚀 Author
Nabil Mohamed
AIM Bootcamp Participant
GitHub: [NabloP](https://github.com/NabloP)