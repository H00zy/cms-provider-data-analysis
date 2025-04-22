import pandas as pd
import numpy as np
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

# Load subset
df = pd.read_csv(r"C:\Users\Admin\PycharmProjects\CMS provider data analysis\Data\cleaned\master_df_predict_subset.csv")
df["experience_years"] = 2022 - df["grd_yr"]

# Prepare X and y
X = df.drop(columns=["npi", "grd_yr", "num_facility_affiliations"])
y = df["num_facility_affiliations"]

# Encode categorical columns
cat_cols = ["pri_spec", "state", "gndr", "telehlth", "med_sch"]
preprocessor = ColumnTransformer([
    ("cat", OneHotEncoder(handle_unknown='ignore'), cat_cols)
], remainder='passthrough')
X_encoded = preprocessor.fit_transform(X)

# Split and train
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model + preprocessor
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/facility_affiliation_model.joblib")
joblib.dump(preprocessor, "models/preprocessor.joblib")

print("✅ Model and preprocessor saved to: models/")
