import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

# 1. Load the cleaned subset
df = pd.read_csv(r"C:\Users\Admin\PycharmProjects\CMS provider data analysis\Data\cleaned\master_df_predict_subset.csv")

# 2. Feature engineering
df["experience_years"] = 2022 - df["grd_yr"]

# 3. Prepare features (X) and target (y)
X = df.drop(columns=["npi", "grd_yr", "num_facility_affiliations"])
y = df["num_facility_affiliations"]

# 4. Preprocess categorical features
cat_cols = ["pri_spec", "state", "gndr", "telehlth", "med_sch"]
preprocessor = ColumnTransformer([
    ("cat", OneHotEncoder(handle_unknown='ignore'), cat_cols)
], remainder='passthrough')

X_encoded = preprocessor.fit_transform(X)

# 5. Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X_encoded, y, test_size=0.2, random_state=42
)

# 6. Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 7. Evaluate predictions
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# 8. Print results
print("✅ Model Trained")
print(f"RMSE: {rmse:.2f}")
print(f"MAE: {mae:.2f}")
print(f"R²: {r2:.4f}")
