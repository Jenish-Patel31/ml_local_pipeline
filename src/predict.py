# src/predict.py
import joblib
import pandas as pd

model = joblib.load("models/decision_tree_model.joblib")

df = pd.read_csv("data/titanic_processed.csv")
X = df.drop(columns=["Survived"])

predictions = model.predict(X)

# Print predictions
print(predictions)
