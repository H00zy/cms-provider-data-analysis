import pandas as pd

# Load the full master DataFrame
df = pd.read_csv(r"C:\Users\Admin\PycharmProjects\CMS provider data analysis\Data\cleaned\master_df.csv")

# Select relevant features
subset = df[[
    'npi', 'pri_spec', 'state', 'gndr', 'grd_yr',
    'telehlth', 'med_sch', 'num_facility_affiliations'
]].copy()

# Drop rows with any missing values (for clean modeling)
subset.dropna(inplace=True)

# Save smaller file
subset.to_csv(r"C:\Users\Admin\PycharmProjects\CMS provider data analysis\Data\cleaned\master_df_predict_subset.csv", index=False)

print("✅ Subset created and saved!")
