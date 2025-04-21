import pandas as pd
import os

# Define file paths
input_paths = {
    "DAC_NationalDownloadableFile": r"C:\Users\Admin\PycharmProjects\CMS provider data analysis\Data\DAC_NationalDownloadableFile.csv",
    "ec_score_file": r"C:\Users\Admin\PycharmProjects\CMS provider data analysis\Data\ec_score_file.csv",
    "Facility_Affiliation": r"C:\Users\Admin\PycharmProjects\CMS provider data analysis\Data\Facility_Affiliation.csv",
    "Utilization": r"C:\Users\Admin\PycharmProjects\CMS provider data analysis\Data\Utilization.csv",
    "ec_public_reporting": r"C:\Users\Admin\PycharmProjects\CMS provider data analysis\Data\ec_public_reporting.csv",
    "grp_public_reporting": r"C:\Users\Admin\PycharmProjects\CMS provider data analysis\Data\grp_public_reporting.csv",
    "grp_public_reporting_cahps": r"C:\Users\Admin\PycharmProjects\CMS provider data analysis\Data\grp_public_reporting_cahps.csv",
    "vg_public_reporting": r"C:\Users\Admin\PycharmProjects\CMS provider data analysis\Data\vg_public_reporting.csv"
}

# Output folder for cleaned files
output_folder = r"C:\Users\Admin\PycharmProjects\CMS provider data analysis\Data\cleaned"
os.makedirs(output_folder, exist_ok=True)

def clean_column_names(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.replace(r"\s+", "_", regex=True)
        .str.replace(r"[^a-zA-Z0-9_]", "", regex=True)
        .str.lower()
    )
    return df

def clean_file(name, path):
    try:
        df = pd.read_csv(path, encoding="utf-8", low_memory=False)
    except UnicodeDecodeError:
        df = pd.read_csv(path, encoding="ISO-8859-1", low_memory=False)

    original_shape = df.shape

    df = clean_column_names(df)

    # Drop rows with missing NPIs if the column exists
    if "npi" in df.columns:
        df = df[df["npi"].notnull()]

    cleaned_shape = df.shape

    print(f"{name}: Cleaned {original_shape[0] - cleaned_shape[0]} rows with missing NPI. Final shape: {cleaned_shape}")

    # Save cleaned version
    output_path = os.path.join(output_folder, f"{name}_cleaned.csv")
    df.to_csv(output_path, index=False)
    print(f"Saved cleaned file to: {output_path}\n")

    return df

# Clean all files
cleaned_dataframes = {}
for name, path in input_paths.items():
    print(f"Processing file: {name}")
    df_cleaned = clean_file(name, path)
    cleaned_dataframes[name] = df_cleaned
