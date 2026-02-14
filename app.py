import streamlit as st
import pandas as pd
import pickle

# Load model and feature columns
with open("model_dummies.pkl", "rb") as f:
    model = pickle.load(f)

with open("dummy_columns.pkl", "rb") as f:
    dummy_columns = pickle.load(f)

st.title("🚚 Delivery Time Prediction App")

# User inputs
distance = st.number_input("Distance (km)", min_value=0.0, value=5.0)

weather = st.selectbox(
    "Weather",
    ["Sunny", "Rainy", "Foggy", "Stormy"]
)

traffic = st.selectbox(
    "Traffic Level",
    ["Low", "Medium", "High"]
)

time_of_day = st.selectbox(
    "Time of Day",
    ["Morning", "Afternoon", "Evening", "Night"]
)

vehicle = st.selectbox(
    "Vehicle Type",
    ["Bike", "Scooter", "Car"]
)

prep_time = st.number_input("Preparation Time (minutes)", min_value=0, value=15)

experience = st.number_input("Courier Experience (years)", min_value=0, value=2)

if st.button("Predict Delivery Time"):

    # Create dataframe (NO Order_ID)
    input_data = pd.DataFrame({
        "Distance_km": [distance],
        "Weather": [weather],
        "Traffic_Level": [traffic],
        "Time_of_Day": [time_of_day],
        "Vehicle_Type": [vehicle],
        "Preparation_Time_min": [prep_time],
        "Courier_Experience_yrs": [experience]
    })

    # Apply get_dummies
    input_data = pd.get_dummies(input_data)

    # Align columns EXACTLY as training
    input_data = input_data.reindex(columns=dummy_columns, fill_value=0)

    # Predict
    prediction = model.predict(input_data)

    st.success(f"📦 Estimated Delivery Time: {round(prediction[0], 2)} minutes")
