import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

# 1. Load subset
df = pd.read_csv(r"C:\Users\Admin\PycharmProjects\CMS provider data analysis\Data\cleaned\master_df_predict_subset.csv")
df["experience_years"] = 2022 - df["grd_yr"]

# 2. Features/Target
X = df.drop(columns=["npi", "grd_yr", "num_facility_affiliations"])
y = df["num_facility_affiliations"]

# 3. Encode
cat_cols = ["pri_spec", "state", "gndr", "telehlth", "med_sch"]
preprocessor = ColumnTransformer([
    ("cat", OneHotEncoder(handle_unknown='ignore'), cat_cols)
], remainder='passthrough')

X_encoded = preprocessor.fit_transform(X)

# 4. Train model
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 5. Feature Names
encoded_features = preprocessor.named_transformers_["cat"].get_feature_names_out(cat_cols)
all_feature_names = np.concatenate([encoded_features, ["experience_years"]])

# 6. Feature Importances
importances = model.feature_importances_
indices = np.argsort(importances)[-15:]

# 7. Plot
plt.figure(figsize=(10, 6))
plt.barh(range(len(indices)), importances[indices], align='center')
plt.yticks(range(len(indices)), all_feature_names[indices])
plt.xlabel("Feature Importance")
plt.title("Top 15 Important Features Predicting Facility Affiliations")
plt.tight_layout()
plt.savefig(r"C:\Users\Admin\PycharmProjects\CMS provider data analysis\outputs\feature_importance.png")
plt.show()

print("✅ Plot saved to: outputs/feature_importance.png")
