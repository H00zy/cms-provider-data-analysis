# CMS Provider Data Analysis (2022)

This project performs data cleaning, integration, visualization, and exploratory modeling using CMS public data for clinicians. It was developed as part of a **pre-assessment for a Medical Data AI Manager role**, demonstrating pipeline design, data QA, and delivery of actionable insights.

---

## 📌 Objective

- Audit CMS clinician-level datasets (2022) for data quality and structural integrity  
- Assess MIPS performance distribution across specialties  
- Prepare deliverables including: visual reports, code, and documentation  
- (Optional Next Step) Build a predictive model to estimate facility affiliations based on clinician metadata  

---

## 📁 Project Structure

cms-provider-data-analysis/ ├── code/ │ ├── CMS_Cleaning_Assessment.py # Initial audit script │ ├── clean_all_files.py # Cleans and standardizes all files │ ├── integrate_cms_data.py # Joins datasets on NPI │ └── generate_mips_graph.py # Creates MIPS by specialty graph │ ├── outputs/ │ ├── mips_by_specialty.png │ └── MIPS_By_Specialty_Summary.pptx │ ├── data/ # Raw & cleaned data (excluded from GitHub) ├── .gitignore ├── README.md └── requirements.txt


---

## 📊 Deliverables

- ✅ Initial cleaning audit with summary tables and charts  
- ✅ Integrated master dataset (local-only due to size)  
- ✅ Specialty-based MIPS performance visualization  
- ✅ PowerPoint slide summarizing insights  
- ✅ GitHub repo with reproducible codebase  
- ⏳ Next (optional): ML prediction model for facility affiliation count

---

## 🛠️ Installation

Install dependencies locally:

```bash
pip install -r requirements.txt


## 🚫 Data Notice

Due to GitHub's file size restrictions, all .csv source data and intermediate artifacts are excluded. You can regenerate them by running the scripts locally.
## 👨‍💻 Author

Hazzaa Alghamdi
Digital healthcare innovator | Python-powered insights
https://github.com/H00zy


---
