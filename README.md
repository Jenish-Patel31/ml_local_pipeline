# 🚀 Machine Learning Pipeline Project  
Welcome to the **Machine Learning Pipeline Project**! This project is a **local ML pipeline** designed to train and deploy a machine learning model with a simple **HTML, CSS, and JavaScript-based GUI** for making predictions.  

## 🌟 **Project Overview**  

This project follows a structured **ML workflow**, including:  
✅ **Data Preprocessing** – Cleaning & preparing data  
✅ **Model Training** – Using a Machine Learning algorithm  
✅ **Model Deployment** – Running a Flask API  
✅ **User Interface** – A simple **HTML form** for users to input data and get predictions  

The model used here is trained to predict survival based on the **Titanic dataset**.

## 🛠 **Tech Stack**  

🔹 **Python** – Core language for ML & backend  
🔹 **Flask** – Lightweight web framework for API  
🔹 **scikit-learn** – For ML model training  
🔹 **Pandas & NumPy** – Data processing  
🔹 **HTML, CSS, JavaScript** – Frontend for the GUI  
🔹 **Git & GitHub** – Version control & collaboration  

## 🚀 **Setup & Run Locally**  

###  **1. Clone the Repository**  

```
git clone https://github.com/Jenish-Patel31/ml_local_pipeline.git
cd ml_local_pipeline
```

###  **2. Create a Virtual Environment (Recommended)**  
```
python3 -m venv ml_env
source ml_env/bin/activate  # On Windows: ml_env\Scripts\activate
```

###  **3. Install Dependencies**  
```
pip install -r requirements.txt
```

###  **4. Run the Flask API**  
```
python app.py
```
The API should now be running at http://127.0.0.1:5000 🎉

## 🌍 Frontend: Access the Web Interface
Simply open ``templates/index.html`` in your browser.

- Enter values into the form
- Click Submit
- Get the prediction instantly!
- 
Alternatively, if running with Flask, access the UI at:
👉 http://127.0.0.1:5000/


## 📜 API Usage
The ML model is exposed via a Flask API. You can send POST requests to make predictions.

### Endpoint:
```
POST /predict 
```
### Request Format (JSON)
```
{
    "Pclass": 3,
    "Sex": 1,
    "Age": 22,
    "SibSp": 1,
    "Parch": 0,
    "Fare": 7.25,
    "Embarked": 2
}
```

### Response Format
```
{
    "prediction": [0]  // 0 = Not Survived, 1 = Survived
}
```

## 📌 Project Structure

```
ml_local_pipeline/
│── app.py               # Flask API
│── model.pkl            # Trained ML model
│── requirements.txt      # Dependencies
│── static/
│   ├── css/styles.css    # Styles for frontend
│── templates/
│   ├── index.html        # User interface
└── README.md             # This file!

```

## 💡 Future Improvements

- Improve UI with better design
- Deploy using Docker & Cloud for scalability
- Extend ML model to predict other datasets


## 📞 Contact  
👨‍💻 **Author** – Jenish Patel  
🔗 **GitHub** – Jenish-Patel31  
🔗 **Linkedin** – jenish-patel-31k  
✉️ **Email** – jenishkp07@gmail.com




