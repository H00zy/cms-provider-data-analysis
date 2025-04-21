import pandas as pd
import os

# Set cleaned data folder
cleaned_path = r"/Data/cleaned"

# Load cleaned CSVs
national_df = pd.read_csv(os.path.join(cleaned_path, "DAC_NationalDownloadableFile_cleaned.csv"))
mips_df = pd.read_csv(os.path.join(cleaned_path, "ec_score_file_cleaned.csv"))
facility_df = pd.read_csv(os.path.join(cleaned_path, "Facility_Affiliation_cleaned.csv"))
utilization_df = pd.read_csv(os.path.join(cleaned_path, "Utilization_cleaned.csv"))

# --- Prepare individual datasets ---

## 1. Reduce MIPS to NPI-level scores
mips_reduced = mips_df.groupby("npi").agg({
    "final_mips_score": "mean",
    "quality_category_score": "mean",
    "pi_category_score": "mean",
    "ia_category_score": "mean",
    "cost_category_score": "mean"
}).reset_index()

## 2. Count facility affiliations per NPI
facility_summary = facility_df.groupby("npi").size().reset_index(name="num_facility_affiliations")

## 3. Summarize utilization metrics per NPI
utilization_summary = utilization_df.groupby("npi").agg({
    "count": "sum",                      # total procedures
    "percentile": "mean"                # average experience level
}).reset_index().rename(columns={
    "count": "total_procedures",
    "percentile": "avg_percentile"
})

# --- Merge all data ---
master_df = national_df.copy()

# Merge one by one
master_df = master_df.merge(mips_reduced, on="npi", how="left")
master_df = master_df.merge(facility_summary, on="npi", how="left")
master_df = master_df.merge(utilization_summary, on="npi", how="left")

# Create 'experience_years' column if graduation year exists
if "grd_yr" in master_df.columns:
    master_df["experience_years"] = 2025 - master_df["grd_yr"]

# Optional: Fill missing affiliation counts with 0
master_df["num_facility_affiliations"] = master_df["num_facility_affiliations"].fillna(0).astype(int)

# Save the master file
output_path = os.path.join(cleaned_path, "master_df.csv")
master_df.to_csv(output_path, index=False)

print(f"\n✅ master_df.csv created at: {output_path}")
print(f"Shape: {master_df.shape}")
print("Columns:", list(master_df.columns))
