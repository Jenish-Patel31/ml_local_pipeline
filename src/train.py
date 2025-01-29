# src/train.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
import joblib

print(f"installation done")


df=pd.read_csv("data/titanic_processed.csv")
# print(df.head())
X=df.drop(columns=["Survived"])
# print(X)
y=df['Survived']
# print(y)


X_train,X_test,y_train,y_test =train_test_split(X,y,test_size=0.2,random_state=42)
# print(X_train)

# model=DecisionTreeClassifier(random_state=42)
# model.fit(X_train,y_train)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

print(f"Training done")

# Save the trained model
joblib.dump(model, "models/decision_tree_model.joblib")

print("Model saved successfully!")

y_pred=model.predict(X_test)


print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:")
print(classification_report(y_test, y_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))




plt.figure(figsize=(12,9))
plot_tree(model, filled=True, feature_names=X.columns, class_names=["Not Survived", "Survived"], rounded=True)
plt.show()

