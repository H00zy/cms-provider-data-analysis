# 📊 CMS Provider Data Analysis & Chest X-ray Classification (2022–2025)

This repository includes two end-to-end projects developed for pre-assessment tasks in a **Medical Data AI Manager** role. The first task focuses on CMS clinician data processing and predictive modeling, while the second tackles medical image classification using the NIH Chest X-ray dataset.

---

## 📌 Overview

### 🧾 Task 1: CMS Provider Data Analysis (2022)
- Audit CMS clinician-level datasets (2022) for data quality and structural integrity  
- Assess MIPS performance distribution across specialties  
- Build a predictive model to estimate the number of facility affiliations per clinician  
- Deliver reproducible analysis and visual summaries  

### 🩻 Task 2: Chest X-ray Image Classification (NIH Sample Dataset)
- Develop a deep learning model for thoracic disease classification using NIH Chest X-ray samples  
- Apply Grad-CAM to highlight areas influencing predictions  
- Evaluate using precision, recall, F1-score, confusion matrix, and ROC curves  
- Generate individual and batch Grad-CAM overlays for interpretability  

---

## 📁 Project Structure

cms-provider-data-analysis/ ├── Code/ │ ├── CMS_Cleaning_Assessment.py │ ├── integrate_cms_data.py │ └── ... ├── ChestXray_Classification/ │ ├── code/ │ │ ├── prepare_data.py │ │ ├── train_model.py │ │ ├── evaluate_model.py │ │ ├── generate_gradcam.py │ │ ├── generate_batch_gradcam.py │ │ └── gradcam_visualization.py │ ├── data/ (sample images and processed CSVs) │ ├── outputs/ │ │ ├── gradcam_overlay.png │ │ ├── gradcam_samples/ │ │ ├── confusion_matrix.png │ │ ├── classification_report.txt │ │ └── roc_curves.png │ ├── models/ ├── outputs/ │ ├── MIPS_By_Specialty_Summary.pptx │ ├── CMS_Modeling_Report.pdf │ └── CMS_Task_1_Submission_Summary.pdf

---

## ✅ Deliverables

### Task 1: CMS Data
- ✅ Initial cleaning audit with summary tables
- ✅ Integrated dataset with multiple sources
- ✅ MIPS by specialty visualization
- ✅ Random Forest model to predict facility affiliations
- ✅ Feature importance analysis
- ✅ Full report and presentation summary
- ✅ Model artifacts available via GitHub Release

### Task 2: Chest X-ray Model
- ✅ Stratified sampling, resizing, and augmentation
- ✅ Class-rebalanced ResNet50 model with weighted loss
- ✅ Model evaluation with classification report and ROC
- ✅ Grad-CAM (single + batch) overlays for interpretation
- ✅ Final report with heatmaps and performance metrics
- ✅ Slide deck summarizing findings

---

## 📦 Model Artifacts

Model files are available in [📥 GitHub Release v1.0](https://github.com/H00zy/cms-provider-data-analysis/releases/tag/v1.0)

Includes:
- `facility_affiliation_model.joblib` (Task 1)
- `preprocessor.joblib`
- `best_model.pth` (Task 2, ResNet50 trained weights)

---

## 🛠️ Installation

bash
pip install -r requirements.txt


## 🚫 Data Notice

Raw .csv files and model binaries are excluded from the GitHub repo due to file size limitations. All artifacts can be reproduced using the scripts provided.

## 👨‍💻 Author

Hazzaa Alghamdi
Digital healthcare innovator | AI-driven decision maker | Python-powered insights
🔗 github.com/H00zy


---
