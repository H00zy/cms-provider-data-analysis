# 📊 CMS Provider Data Analysis (2022)

This project performs data cleaning, integration, visualization, and exploratory modeling using CMS public data for clinicians. It was developed as part of a **pre-assessment for a Medical Data AI Manager role**, demonstrating pipeline design, data QA, modeling, and delivery of actionable insights.

---

## 📌 Objective

- Audit CMS clinician-level datasets (2022) for data quality and structural integrity  
- Assess MIPS performance distribution across specialties  
- Build a predictive model to estimate the number of facility affiliations per clinician  
- Prepare deliverables including visual reports, codebase, model, and documentation  

---

## 📁 Project Structure

cms-provider-data-analysis/ ├── Code/ │ ├── CMS_Cleaning_Assessment.py # Initial QA audit │ ├── clean_all_files.py # Cleans and standardizes all files │ ├── integrate_cms_data.py # Joins datasets on NPI │ ├── generate_mips_graph.py # Creates MIPS score visualization │ ├── predict_facility_affiliations.py # Trains RandomForest model │ ├── analyze_feature_importance.py # Generates feature importance chart │ ├── save_model.py # Saves trained model artifacts │ └── Sample_subset_of_master_file.py # Prepares modeling subset │ ├── Data/ # Raw & cleaned data (excluded from GitHub) ├── outputs/ │ ├── mips_by_specialty.png │ ├── MIPS_By_Specialty_Summary.pptx │ └── feature_importance.png │ ├── models/ (excluded) → see release ├── requirements.txt └── README.md



---

## 📊 Deliverables

- ✅ Initial cleaning audit with summary tables and missingness stats  
- ✅ Integrated master dataset (local-only due to file size limits)  
- ✅ MIPS performance visualization by specialty  
- ✅ Feature importance graph for model explanation  
- ✅ PowerPoint summaries for both MIPS and Modeling insights  
- ✅ Trained model & preprocessor pipeline (shared via GitHub Releases)  
- ✅ GitHub repo for review and reproducibility  

---

## 📦 Model Artifacts

Model files are too large for the repo and are included in this [📥 GitHub Release v1.0](https://github.com/H00zy/cms-provider-data-analysis/releases/tag/v1.0)

### 🔍 Files:
- `facility_affiliation_model.joblib` (Random Forest model ~892MB)  
- `preprocessor.joblib` (OneHotEncoder pipeline)  

> Use directly with the provided `predict_facility_affiliations.py` or regenerate using the modeling subset.

---

## 🛠️ Installation

Install requirements:

```bash
pip install -r requirements.txt

## 🚫 Data Notice

Due to GitHub’s file size restrictions, raw .csv files and large model binaries are excluded from version control. You can recreate all artifacts by running the scripts locally using the shared logic.

## 👨‍💻 Author

Hazzaa Alghamdi
Digital healthcare innovator | AI-driven decision maker | Python-powered insights
🔗 github.com/H00zy


---
