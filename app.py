# ============================================================
# 🚚 Delivery Time Intelligence System (Enterprise Edition)
# Developed by Akshit Gajera
# ============================================================

import streamlit as st
import pandas as pd
import pickle
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# ------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------
st.set_page_config(
    page_title="Delivery Time Intelligence",
    page_icon="🚚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------------------------------------------
# LOAD MODEL
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
# DARK ENTERPRISE THEME
# ------------------------------------------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    font-family: 'Segoe UI', sans-serif;
}
.main-header {
    font-size: 2.5rem;
    font-weight: bold;
    text-align: center;
}
.sub-header {
    text-align: center;
    color: #94a3b8;
    margin-bottom: 2rem;
}
.card {
    background: #1f2937;
    padding: 25px;
    border-radius: 20px;
    margin-bottom: 25px;
}
.kpi-value {
    font-size: 60px;
    font-weight: 800;
    text-align: center;
    color: #22d3ee;
}
.kpi-label {
    text-align: center;
    font-size: 18px;
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
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# SIDEBAR
# ------------------------------------------------------------
with st.sidebar:
    st.markdown("## 🚚 Project Overview")
    st.info("""
    Machine Learning-Based Delivery Time Prediction
    
    Algorithm: Linear Regression  
    Encoding: One-Hot Encoding  
    Features: 7
    """)

    st.markdown("---")
    st.markdown("## 📊 Model Info")
    st.metric("Model Type", "Linear Regression")
    st.metric("Encoding", "One-Hot")
    st.metric("Deployment", "Streamlit")

# ------------------------------------------------------------
# HEADER
# ------------------------------------------------------------
st.markdown('<div class="main-header">🚚 Delivery Time Intelligence Platform</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">AI-Powered Logistics Optimization System</div>', unsafe_allow_html=True)

# ------------------------------------------------------------
# TABS STRUCTURE
# ------------------------------------------------------------
tab1, tab2, tab3 = st.tabs([
    "Prediction",
    "Analytics",
    "Model Insights"
])

# ============================================================
# TAB 1 - PREDICTION (ONLY IMPROVED LAYOUT)
# ============================================================
with tab1:

    st.markdown("### 📦 Order Details")

    # Compact grid layout
    col1, col2, col3 = st.columns(3)

    with col1:
        distance = st.number_input("Distance (km)", 0.0, 100.0, 5.0)
        weather = st.selectbox("Weather", ["Sunny", "Rainy", "Foggy", "Stormy"])

    with col2:
        traffic = st.selectbox("Traffic Level", ["Low", "Medium", "High"])
        time_of_day = st.selectbox("Time of Day", ["Morning", "Afternoon", "Evening", "Night"])

    with col3:
        vehicle = st.selectbox("Vehicle Type", ["Bike", "Scooter", "Car"])
        prep_time = st.number_input("Preparation Time (minutes)", 0, 120, 15)

    experience = st.number_input("Courier Experience (years)", 0, 20, 2)

    st.markdown("---")

    predict = st.button("🚀 Run Prediction")

    # RESULT SHOWN BELOW (NOT RIGHT SIDE)
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

        st.session_state["predicted_time"] = predicted_time
        st.session_state["distance"] = distance
        st.session_state["prep_time"] = prep_time

        st.markdown(
            f"""
            <div class="card">
                <div class="kpi-value">{predicted_time}</div>
                <div class="kpi-label">Estimated Delivery Time (Minutes)</div>
            </div>
            """,
            unsafe_allow_html=True
        )

# ============================================================
# TAB 2 - ANALYTICS (UNCHANGED)
# ============================================================
with tab2:

    if "predicted_time" in st.session_state:

        st.markdown("### 📊 Distance vs Delivery Time Simulation")

        distances = np.linspace(1, 20, 20)
        simulated_times = []

        for d in distances:
            simulated_times.append(
                st.session_state["predicted_time"] * (d / st.session_state["distance"])
            )

        fig = px.line(
            x=distances,
            y=simulated_times,
            labels={"x":"Distance (km)","y":"Estimated Time (min)"},
            title="Impact of Distance on Delivery Time"
        )
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("### 📈 Preparation Time Impact")

        prep_range = np.linspace(5, 40, 10)
        prep_effect = st.session_state["predicted_time"] + (
            prep_range - st.session_state["prep_time"]
        )

        fig2 = px.line(
            x=prep_range,
            y=prep_effect,
            labels={"x":"Preparation Time (min)","y":"Estimated Delivery Time"},
            title="Preparation Time Sensitivity"
        )
        st.plotly_chart(fig2, use_container_width=True)

    else:
        st.info("Run prediction first to see analytics.")

# ============================================================
# TAB 3 - MODEL INSIGHTS (UNCHANGED)
# ============================================================
with tab3:

    st.markdown("### 🧠 Why Linear Regression?")

    st.success("""
    • Simple and interpretable  
    • Fast inference  
    • Suitable for continuous prediction  
    • Easy integration with One-Hot Encoding  
    """)

    st.markdown("### 📌 Business Insights")

    st.write("""
    • Distance and Preparation Time have strongest impact  
    • Traffic & Weather introduce variance  
    • Experience reduces delay risk  
    • Vehicle type affects speed efficiency  
    """)

# ------------------------------------------------------------
# FOOTER
# ------------------------------------------------------------
st.markdown("---")
st.markdown("<div style='text-align:center;color:#64748b;'>© 2026 Akshit Gajera | ML Delivery Intelligence Platform</div>", unsafe_allow_html=True)
