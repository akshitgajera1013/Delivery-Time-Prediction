# ============================================================
# 🚚 Delivery Time Intelligence System
# Developed by Akshit Gajera
# ============================================================

import streamlit as st
import pandas as pd
import pickle

# ------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------
st.set_page_config(
    page_title="Delivery Time Intelligence",
    page_icon="🚚",
    layout="wide"
)

# ------------------------------------------------------------
# LOAD MODEL & DUMMY COLUMNS
# ------------------------------------------------------------
@st.cache_resource
def load_files():
    with open("model_dummies.pkl", "rb") as f:
        model = pickle.load(f)
    with open("dummy_columns.pkl", "rb") as f:
        dummy_columns = pickle.load(f)
    return model, dummy_columns

model, dummy_columns = load_files()

# ------------------------------------------------------------
# PREMIUM DARK DASHBOARD CSS
# ------------------------------------------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    font-family: 'Segoe UI', sans-serif;
}

.main-container {
    background: #111827;
    padding: 40px;
    border-radius: 25px;
    box-shadow: 0 20px 60px rgba(0,0,0,0.6);
    margin-top: 30px;
}

.header-strip {
    background: linear-gradient(90deg,#2563eb,#06b6d4);
    padding: 20px 30px;
    border-radius: 18px;
    color: white;
    font-size: 26px;
    font-weight: 700;
    margin-bottom: 30px;
}

.card {
    background: #1f2937;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.5);
    margin-bottom: 25px;
}

.kpi-value {
    font-size: 65px;
    font-weight: 800;
    text-align: center;
    color: #22d3ee;
}

.kpi-label {
    text-align: center;
    font-size: 20px;
    color: #cbd5e1;
}

.stButton>button {
    width: 100%;
    height: 55px;
    border-radius: 15px;
    font-weight: bold;
    font-size: 18px;
    background: linear-gradient(90deg,#22d3ee,#3b82f6);
    border: none;
    color: black;
}

.footer {
    text-align: center;
    color: #64748b;
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# MAIN CONTAINER
# ------------------------------------------------------------
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.markdown('<div class="header-strip">Machine Learning-Based Delivery Time Prediction System</div>', unsafe_allow_html=True)

left, right = st.columns([1,1.2])

# ------------------------------------------------------------
# LEFT PANEL – INPUT SECTION
# ------------------------------------------------------------
with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📦 Delivery Order Details")

    distance = st.number_input("Distance (km)", min_value=0.0, value=5.0)

    weather = st.selectbox("Weather", ["Sunny", "Rainy", "Foggy", "Stormy"])
    traffic = st.selectbox("Traffic Level", ["Low", "Medium", "High"])
    time_of_day = st.selectbox("Time of Day", ["Morning", "Afternoon", "Evening", "Night"])
    vehicle = st.selectbox("Vehicle Type", ["Bike", "Scooter", "Car"])

    prep_time = st.number_input("Preparation Time (minutes)", min_value=0, value=15)
    experience = st.number_input("Courier Experience (years)", min_value=0, value=2)

    predict = st.button("🚀 Predict Delivery Time")

    st.markdown('</div>', unsafe_allow_html=True)

# ------------------------------------------------------------
# RIGHT PANEL – ANALYTICS & OUTPUT
# ------------------------------------------------------------
with right:

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📊 Model Overview")

    col1, col2, col3 = st.columns(3)
    col1.metric("Algorithm", "Linear Regression")
    col2.metric("Features", "7")
    col3.metric("Encoding", "One-Hot")

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("⏱ Prediction Output")
    output_placeholder = st.empty()
    st.markdown('</div>', unsafe_allow_html=True)

# ------------------------------------------------------------
# PREDICTION LOGIC
# ------------------------------------------------------------
if predict:
    input_data = pd.DataFrame({
        "Distance_km": [distance],
        "Weather": [weather],
        "Traffic_Level": [traffic],
        "Time_of_Day": [time_of_day],
        "Vehicle_Type": [vehicle],
        "Preparation_Time_min": [prep_time],
        "Courier_Experience_yrs": [experience]
    })

    input_data = pd.get_dummies(input_data)
    input_data = input_data.reindex(columns=dummy_columns, fill_value=0)

    prediction = model.predict(input_data)
    predicted_time = round(prediction[0], 2)

    output_placeholder.markdown(
        f'<div class="kpi-value">{predicted_time}</div>'
        f'<div class="kpi-label">Estimated Delivery Time (Minutes)</div>',
        unsafe_allow_html=True
    )

st.markdown('</div>', unsafe_allow_html=True)

# ------------------------------------------------------------
# FOOTER
# ------------------------------------------------------------
st.markdown('<div class="footer">© 2026 Akshit Gajera | ML Delivery Intelligence System</div>', unsafe_allow_html=True)
