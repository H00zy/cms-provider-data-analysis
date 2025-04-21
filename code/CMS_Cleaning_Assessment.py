import pandas as pd
import matplotlib.pyplot as plt
import os

# Define file paths
file_paths = {
    "DAC_NationalDownloadableFile": r"C:\Users\Admin\PycharmProjects\CMS provider data analysis\Data\DAC_NationalDownloadableFile.csv",
    "ec_score_file": r"C:\Users\Admin\PycharmProjects\CMS provider data analysis\Data\ec_score_file.csv",
    "Facility_Affiliation": r"C:\Users\Admin\PycharmProjects\CMS provider data analysis\Data\Facility_Affiliation.csv",
    "Utilization": r"C:\Users\Admin\PycharmProjects\CMS provider data analysis\Data\Utilization.csv",
    "ec_public_reporting": r"C:\Users\Admin\PycharmProjects\CMS provider data analysis\Data\ec_public_reporting.csv",
    "grp_public_reporting": r"C:\Users\Admin\PycharmProjects\CMS provider data analysis\Data\grp_public_reporting.csv",
    "grp_public_reporting_cahps": r"C:\Users\Admin\PycharmProjects\CMS provider data analysis\Data\grp_public_reporting_cahps.csv",
    "vg_public_reporting": r"C:\Users\Admin\PycharmProjects\CMS provider data analysis\Data\vg_public_reporting.csv"
}

# Cleaning assessment function
def assess_data_cleaning(filepath):
    try:
        df = pd.read_csv(filepath, encoding='utf-8', low_memory=False)
    except UnicodeDecodeError:
        df = pd.read_csv(filepath, encoding='ISO-8859-1', low_memory=False)

    report = {}
    report["Shape"] = df.shape
    report["Duplicated Rows"] = df.duplicated().sum()
    report["Missing Values (Total)"] = df.isnull().sum().sum()
    report["% Missing Values"] = round((df.isnull().sum().sum() / (df.shape[0] * df.shape[1])) * 100, 2)
    report["Columns with Missing Values"] = df.columns[df.isnull().any()].tolist()
    report["Suspicious Column Names"] = [col for col in df.columns if "\t" in col or col.strip() != col]
    return report, df

# Run assessment for all files
cleaning_reports = {}
missing_summary = []
for name, path in file_paths.items():
    report, _ = assess_data_cleaning(path)
    cleaning_reports[name] = report
    missing_summary.append({
        "File": name,
        "Rows": report["Shape"][0],
        "Cols": report["Shape"][1],
        "Total Missing": report["Missing Values (Total)"],
        "Missing %": report["% Missing Values"],
        "Cols Needing Cleaning": len(report["Suspicious Column Names"])
    })

# Convert to DataFrame for plotting
summary_df = pd.DataFrame(missing_summary).sort_values(by="Total Missing", ascending=False)

# Print assessment as a block
for name, report in cleaning_reports.items():
    print(f"File: {name}")
    print("-" * (len(name) + 6))
    for key, value in report.items():
        print(f"{key}:")
        if isinstance(value, list):
            for item in value:
                print(f" - {item}")
        else:
            print(f" {value}")
    print("\n")

# Plotting total and % missing values per file
plt.figure(figsize=(12, 6))
plt.bar(summary_df["File"], summary_df["Total Missing"], color='skyblue')
plt.xticks(rotation=45, ha="right")
plt.ylabel("Total Missing Values")
plt.title("Missing Data by File")
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
plt.bar(summary_df["File"], summary_df["Missing %"], color='salmon')
plt.xticks(rotation=45, ha="right")
plt.ylabel("Missing Values (%)")
plt.title("Missing Value Percentage by File")
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
plt.bar(summary_df["File"], summary_df["Cols Needing Cleaning"], color='orange')
plt.xticks(rotation=45, ha="right")
plt.ylabel("# of Columns Needing Cleaning")
plt.title("Suspicious Column Names per File")
plt.tight_layout()
plt.show()
