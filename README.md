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
solar-challenge-week1/
solar-challenge-week1/
├── .gitignore                     # Git ignores tracked environment/data
├── LICENSE                        # Open source license
├── project-tree.txt              # Auto-generated tree snapshot (optional)
├── README.md                      # Project overview, setup, and status
├── requirements.txt              # Python dependencies for reproducibility
│
├── .github/
│   └── workflows/
│       ├── ci.yml                # Linting, install checks, CI setup
│       └── unittests.yml         # Test suite CI runner (placeholder for now)
│
├── .vscode/
│   └── settings.json             # IDE configuration (e.g., Python path, linting)
│
├── notebooks/                    # Jupyter notebooks for EDA, analysis
│
├── scripts/                      # Utility and one-off scripts
│   ├── README.md                 # Script documentation (optional)
│   ├── __init__.py              # Makes `scripts` a module
│   └── generate_tree.py         # Generates folder structure for README (excludes `venv`)
│
├── src/                          # Source code for main pipeline/modules
│   └── (to be added)            # Placeholder – will hold reusable code
│
├── tests/                        # Unit tests and test configs
│   └── __init__.py              # Test package initializer
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