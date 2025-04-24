# 📊 CMS Provider Data Analysis (2022)

This project performs data cleaning, integration, visualization, and exploratory modeling using CMS public data for clinicians. It was developed as part of a **pre-assessment for a Medical Data AI Manager role**, demonstrating pipeline design, data QA, modeling, and delivery of actionable insights.

## 📌 Objective

- Audit CMS clinician-level datasets (2022) for data quality and structural integrity  
- Assess MIPS performance distribution across specialties  
- Build a predictive model to estimate the number of facility affiliations per clinician  
- Prepare deliverables including visual reports, codebase, model, and documentation  

## 📁 Project Structure

cms-provider-data-analysis/
├── Code/
│   ├── CMS_Cleaning_Assessment.py
│   ├── clean_all_files.py
│   ├── integrate_cms_data.py
│   ├── generate_mips_graph.py
│   ├── predict_facility_affiliations.py
│   ├── analyze_feature_importance.py
│   ├── save_model.py
│   └── Sample_subset_of_master_file.py
├── Data/ (Raw & cleaned CSVs — local only)
├── models/ (excluded from GitHub)
├── outputs/
│   ├── mips_by_specialty.png
│   ├── feature_importance.png
│   └── MIPS_By_Specialty_Summary.pptx
├── requirements.txt
└── README.md

## ✅ Deliverables

- ✅ Initial cleaning audit with summary tables and missingness stats  
- ✅ Integrated master dataset (local-only due to file size limits)  
- ✅ MIPS performance visualization by specialty  
- ✅ Feature importance graph for model explanation  
- ✅ PowerPoint summaries for both MIPS and Modeling insights  
- ✅ Trained model & preprocessor pipeline (shared via GitHub Releases)  
- ✅ GitHub repo for review and reproducibility  

## 📦 Model Artifacts

Model files are included in this [📥 GitHub Release v1.0](https://github.com/H00zy/cms-provider-data-analysis/releases/tag/v1.0)
- `facility_affiliation_model.joblib`  
- `preprocessor.joblib`

## 🛠️ Installation

```bash
pip install -r requirements.txt
```

## 👨‍💻 Author

Hazzaa Alghamdi  
Digital healthcare innovator | AI-driven decision maker | Python-powered insights  
🔗 github.com/H00zy
