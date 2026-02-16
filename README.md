# Delivery-Time-Prediction

Deployment Link :- https://delivery-time-prediction-model.streamlit.app/

# 🚚 Delivery Time Prediction using Machine Learning
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Regression-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-WebApp-red)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)

## 📌 Project Overview
This project predicts the delivery time (in minutes) for an order based on multiple factors such as:
- Distance
- Weather conditions
- Traffic level
- Time of day
- Vehicle type
- Preparation time
- Courier experience
The model is built using **Linear Regression** and deployed with an interactive **Streamlit web application**.

## 🧠 Machine Learning Details
- Model: Linear Regression
- Encoding Method: One-Hot Encoding using `pd.get_dummies()`
- Target Variable: `Delivery_Time_min`
- Model Serialization: Pickle
- Feature Alignment: Saved dummy columns to ensure correct prediction
- Deployment: Streamlit

## 📊 Features Used for Prediction
- Distance_km
- Weather
- Traffic_Level
- Time_of_Day
- Vehicle_Type
- Preparation_Time_min
- Courier_Experience_yrs

## 📂 Project Structure
Delivery-Time-Prediction/
├── app.py
├── model_dummies.pkl
├── dummy_columns.pkl
├── requirements.txt
└── README.md



---

## ▶️ How to Run the Project Locally

1️⃣ Clone the repository:
https://github.com/akshitgajera1013/Delivery-Time-Prediction.git

2️⃣ Navigate to the project folder:
cd Delivery-Time-Prediction

3️⃣ Install dependencies:
pip install -r requirements.txt


4️⃣ Run the Streamlit app:
python -m streamlit run app.py

The app will open automatically in your browser.

## 📦 requirements.txt
streamlit

pandas

numpy

scikit-learn

