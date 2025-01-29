# src/app.py
from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load('models/decision_tree_model.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the JSON data from the request
    data = request.get_json()

    # Convert the data into a DataFrame (or handle it according to the features)
    input_data = pd.DataFrame(data)

    # Predict using the loaded model
    prediction = model.predict(input_data)

    # Send back the prediction as JSON response
    return jsonify({"prediction": prediction.tolist()})

if __name__ == "__main__":
    app.run(debug=True)
