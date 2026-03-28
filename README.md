# Delivery-Time-Prediction

Deployment Link :- https://delivery-time-prediction-model.streamlit.app/

# 🚚 Delivery Time Prediction using Machine Learning
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Regression-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-WebApp-red)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)


📁 Dataset Overview

This project uses a Food Delivery Times Dataset that contains information about delivery operations, including order details, environmental conditions, and courier-related factors. The dataset is designed to analyze and predict food delivery time based on various influencing parameters.

It combines logistical, operational, and external factors to provide insights into how different conditions impact delivery efficiency.

📊 Dataset Summary
| Property        | Value                          |
| --------------- | ------------------------------ |
| Dataset Type    | Food Delivery / Logistics Data |
| Data Type       | Structured (Tabular)           |
| Feature Types   | Numerical + Categorical        |
| Target Variable | Delivery Time                  |
| Task Type       | Regression                     |

🔑 Key Features

The dataset includes important attributes such as:

    Distance (in km)
    Weather Conditions
    Traffic Level
    Time of Day
    Vehicle Type
    Order Preparation Time
    Courier Experience (in years)
    Delivery Time (target variable)

These features help in understanding how external conditions and operational factors affect delivery performance.

🎯 Objective of the Dataset

The primary objective of this dataset is to:

    Analyze factors influencing delivery time
    Predict delivery duration using machine learning models
    Optimize delivery operations
    Improve customer satisfaction through faster deliveries
    
🧠 Analysis Use Cases

This dataset can be used for:
    
    Delivery time prediction
    Logistics optimization
    Traffic and weather impact analysis
    Courier performance evaluation
    Operational efficiency analysis


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

