import pandas as pd
import joblib
from sklearn.ensemble import IsolationForest, RandomForestClassifier
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("data/vehicle_data.csv")

X = df.drop("label", axis=1)
y = df["label"]

# Unsupervised
isolation = IsolationForest(contamination=0.05)
isolation.fit(X)
joblib.dump(isolation, "model/isolation.pkl")

# Supervised RF
rf = RandomForestClassifier()
rf.fit(X, y)
joblib.dump(rf, "model/rf_classifier.pkl")

# Supervised LR
lr = LogisticRegression(max_iter=1000)
lr.fit(X, y)
joblib.dump(lr, "model/lr_classifier.pkl")

print("Models trained successfully.")