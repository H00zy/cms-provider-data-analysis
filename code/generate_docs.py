readme_content = """# CMS Provider Data Analysis (2022)

This project performs cleaning, integration, visualization, and predictive modeling using CMS public data for clinicians.

## 📌 Objective
To analyze 2022 CMS clinician-level data, assess MIPS performance by specialty, and build a predictive model for facility affiliations using specialty, gender, state, and experience.

## 📁 Project Structure

cms-provider-data-analysis/
├── code/
│   ├── clean_all_files.py
│   ├── integrate_cms_data.py
│   └── generate_mips_graph.py
├── outputs/
│   ├── mips_by_specialty.png
│   └── MIPS_By_Specialty_Summary.pptx
├── data/ (excluded from GitHub)
├── .gitignore
├── README.md
└── requirements.txt

## 📊 Deliverables

- ✅ Cleaned CMS datasets
- ✅ Master integrated dataset (local only)
- ✅ MIPS visualization
- ✅ PowerPoint summary
- ✅ (Next) Prediction model

## 🛠️ Installation

pip install -r requirements.txt

## 🚫 Data Notice

CSV files are excluded due to GitHub size limits. Run the scripts locally to regenerate them.

## 👨‍💻 Author

H00zy — Digital healthcare innovator | Python-powered insights
"""

reqs_content = """pandas
matplotlib
seaborn
scikit-learn
python-pptx
openpyxl
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)

with open("requirements.txt", "w", encoding="utf-8") as f:
    f.write(reqs_content)

print("✅ README.md and requirements.txt generated successfully.")
