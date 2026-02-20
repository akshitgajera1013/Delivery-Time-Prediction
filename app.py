# ============================================================
# 🚚 Delivery Time Intelligence System (Enterprise Edition)
# Developed by Akshit Gajera
# Enhanced UI — Industrial Logistics Terminal Aesthetic
# ============================================================

import streamlit as st
import pandas as pd
import pickle
import plotly.graph_objects as go
import numpy as np

# ============================================================
# PAGE CONFIG  —  must be the very first Streamlit call
# ============================================================
st.set_page_config(
    page_title="Delivery Time Intelligence",
    page_icon="🚚",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# LOAD MODEL FILES
# ============================================================
@st.cache_resource
def load_files():
    with open("model_dummies.pkl", "rb") as f:
        model = pickle.load(f)
    with open("dummy_columns.pkl", "rb") as f:
        dummy_columns = pickle.load(f)
    return model, dummy_columns


model, dummy_columns = load_files()

# ============================================================
# PROFESSIONAL ANIMATED THEME  —  Industrial Amber / Orange
# ============================================================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Exo+2:wght@300;400;600;700;900&family=JetBrains+Mono:wght@400;600&family=Barlow+Condensed:wght@400;600;700;900&display=swap');

/* ── VARIABLES ── */
:root {
    --amber:        #f59e0b;
    --amber-dark:   #b45309;
    --amber-glow:   rgba(245,158,11,0.3);
    --orange:       #ea580c;
    --green:        #10b981;
    --red:          #ef4444;
    --dark-950:     #0a0a0a;
    --dark-900:     #111111;
    --dark-800:     #1a1a1a;
    --dark-700:     #222222;
    --dark-600:     #2a2a2a;
    --glass:        rgba(245,158,11,0.04);
    --glass-border: rgba(245,158,11,0.15);
    --glow:         0 0 25px rgba(245,158,11,0.25);
    --text-main:    #f5f0e8;
    --text-muted:   rgba(245,240,232,0.5);
}

/* ── BACKGROUND ── */
.stApp {
    background: var(--dark-950);
    font-family: 'Exo 2', sans-serif;
    overflow-x: hidden;
}

.stApp::before {
    content: '';
    position: fixed;
    inset: 0;
    background:
        radial-gradient(ellipse at 20% 10%, rgba(245,158,11,0.07) 0%, transparent 50%),
        radial-gradient(ellipse at 80% 90%, rgba(234,88,12,0.06) 0%, transparent 50%),
        radial-gradient(ellipse at 50% 50%, rgba(16,185,129,0.02) 0%, transparent 60%);
    pointer-events: none;
    z-index: 0;
    animation: bgShift 10s ease-in-out infinite alternate;
}

@keyframes bgShift {
    0%   { opacity: 0.6; }
    100% { opacity: 1.0; }
}

/* ── DIAGONAL GRID PATTERN ── */
.stApp::after {
    content: '';
    position: fixed;
    inset: 0;
    background-image:
        repeating-linear-gradient(
            45deg,
            rgba(245,158,11,0.015) 0px,
            rgba(245,158,11,0.015) 1px,
            transparent 1px,
            transparent 28px
        );
    pointer-events: none;
    z-index: 0;
}

/* ── MAIN BLOCK ── */
.main .block-container {
    position: relative;
    z-index: 1;
    padding-top: 10px;
    padding-bottom: 40px;
    max-width: 1400px;
}

/* ── HERO HEADER ── */
.hero-wrap {
    position: relative;
    padding: 44px 20px 28px;
    text-align: center;
    animation: heroIn 0.9s cubic-bezier(0.22,1,0.36,1) both;
}

@keyframes heroIn {
    from { opacity: 0; transform: translateY(-24px); }
    to   { opacity: 1; transform: translateY(0); }
}

.hero-eyebrow {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    letter-spacing: 5px;
    color: var(--amber);
    text-transform: uppercase;
    margin-bottom: 10px;
    opacity: 0.8;
    animation: heroIn 0.9s ease both 0.1s;
}

.hero-title {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: clamp(32px, 5vw, 68px);
    font-weight: 900;
    text-transform: uppercase;
    letter-spacing: 4px;
    color: var(--text-main);
    line-height: 1;
    margin-bottom: 6px;
    position: relative;
}

.hero-title span {
    background: linear-gradient(90deg, var(--amber), var(--orange));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    filter: drop-shadow(0 0 20px rgba(245,158,11,0.6));
}

.hero-sub {
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    color: var(--text-muted);
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-top: 10px;
    animation: heroIn 0.9s ease both 0.3s;
}

.hero-divider {
    display: flex;
    align-items: center;
    gap: 16px;
    margin: 18px auto 0;
    max-width: 500px;
}

.hero-divider-line {
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--amber), transparent);
    animation: expandLine 1s ease both 0.5s;
}

@keyframes expandLine {
    from { opacity: 0; transform: scaleX(0); }
    to   { opacity: 1; transform: scaleX(1); }
}

.hero-divider-diamond {
    width: 8px;
    height: 8px;
    background: var(--amber);
    transform: rotate(45deg);
    box-shadow: 0 0 12px var(--amber);
    animation: pulse 2s ease-in-out infinite;
}

@keyframes pulse {
    0%, 100% { box-shadow: 0 0 12px var(--amber); opacity: 1; }
    50%       { box-shadow: 0 0 24px var(--amber); opacity: 0.7; }
}

/* ── TICKER BAR ── */
.ticker-bar {
    background: rgba(245,158,11,0.06);
    border-top: 1px solid rgba(245,158,11,0.12);
    border-bottom: 1px solid rgba(245,158,11,0.12);
    padding: 10px 0;
    overflow: hidden;
    position: relative;
    margin-bottom: 28px;
}

.ticker-inner {
    display: inline-flex;
    gap: 60px;
    animation: ticker 20s linear infinite;
    white-space: nowrap;
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: var(--amber);
    letter-spacing: 2px;
}

@keyframes ticker {
    from { transform: translateX(0); }
    to   { transform: translateX(-50%); }
}

.ticker-item {
    display: inline-flex;
    align-items: center;
    gap: 8px;
}

.ticker-dot {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: var(--amber);
    box-shadow: 0 0 8px var(--amber);
}

/* ── GLASS PANEL ── */
.glass-panel {
    background: var(--glass);
    border: 1px solid var(--glass-border);
    border-radius: 16px;
    padding: 26px;
    margin-bottom: 22px;
    position: relative;
    overflow: hidden;
    transition: all 0.3s ease;
    animation: panelIn 0.6s ease both;
}

@keyframes panelIn {
    from { opacity: 0; transform: translateY(16px); }
    to   { opacity: 1; transform: translateY(0); }
}

.glass-panel::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 4px; height: 100%;
    background: linear-gradient(180deg, var(--amber), var(--orange));
    border-radius: 4px 0 0 4px;
}

.glass-panel::after {
    content: '';
    position: absolute;
    top: 0; left: -100%;
    width: 100%; height: 2px;
    background: linear-gradient(90deg, transparent, var(--amber), transparent);
    animation: scanH 4s linear infinite;
}

@keyframes scanH {
    0%   { left: -100%; }
    100% { left: 100%; }
}

.glass-panel:hover {
    border-color: rgba(245,158,11,0.35);
    box-shadow: var(--glow);
}

/* ── PANEL TITLE ── */
.panel-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    letter-spacing: 3px;
    color: var(--amber);
    text-transform: uppercase;
    margin-bottom: 4px;
    opacity: 0.7;
}

.panel-title {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 22px;
    font-weight: 700;
    color: var(--text-main);
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 0;
}

/* ── INPUT FIELDS ── */
div[data-testid="stNumberInput"] > div > div > input,
div[data-testid="stSelectbox"] > div > div {
    background: rgba(245,158,11,0.04) !important;
    border: 1px solid rgba(245,158,11,0.2) !important;
    border-radius: 10px !important;
    color: var(--text-main) !important;
    font-family: 'Exo 2', sans-serif !important;
    font-size: 15px !important;
    transition: all 0.25s ease !important;
}

div[data-testid="stNumberInput"] > div > div > input:focus {
    border-color: var(--amber) !important;
    box-shadow: 0 0 0 3px rgba(245,158,11,0.15) !important;
    outline: none !important;
}

.stSelectbox label,
.stNumberInput label {
    color: rgba(245,158,11,0.85) !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 11px !important;
    letter-spacing: 1.5px !important;
    text-transform: uppercase !important;
}

/* ── SECTION DIVIDER LABEL ── */
.input-group-label {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 3px;
    color: var(--amber);
    text-transform: uppercase;
    border-bottom: 1px solid rgba(245,158,11,0.15);
    padding-bottom: 8px;
    margin-bottom: 14px;
}

/* ── PREDICT BUTTON ── */
div.stButton > button {
    width: 100% !important;
    background: linear-gradient(135deg, var(--amber) 0%, var(--orange) 100%) !important;
    color: #0a0a0a !important;
    font-family: 'Barlow Condensed', sans-serif !important;
    font-size: 18px !important;
    font-weight: 900 !important;
    letter-spacing: 4px !important;
    text-transform: uppercase !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 16px 40px !important;
    cursor: pointer !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 0 30px rgba(245,158,11,0.35) !important;
}

div.stButton > button:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 0 50px rgba(245,158,11,0.55), 0 8px 20px rgba(0,0,0,0.4) !important;
}

div.stButton > button:active {
    transform: translateY(0) !important;
}

/* ── RESULT KPI BOX ── */
.kpi-box {
    background: linear-gradient(135deg, #1a1000, #2a1a00);
    border: 1px solid rgba(245,158,11,0.4);
    border-radius: 20px;
    padding: 44px 30px;
    text-align: center;
    position: relative;
    overflow: hidden;
    animation: kpiPop 0.5s cubic-bezier(0.175,0.885,0.32,1.275) both;
    box-shadow: 0 0 50px rgba(245,158,11,0.2), inset 0 0 50px rgba(245,158,11,0.04);
}

@keyframes kpiPop {
    from { opacity: 0; transform: scale(0.85); }
    to   { opacity: 1; transform: scale(1); }
}

.kpi-box::before {
    content: '';
    position: absolute;
    top: -50%; left: -50%;
    width: 200%; height: 200%;
    background: conic-gradient(from 0deg, transparent 0deg, rgba(245,158,11,0.04) 60deg, transparent 120deg);
    animation: spinBg 8s linear infinite;
}

@keyframes spinBg {
    from { transform: rotate(0deg); }
    to   { transform: rotate(360deg); }
}

.kpi-value {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: clamp(52px, 8vw, 96px);
    font-weight: 900;
    line-height: 1;
    background: linear-gradient(135deg, var(--amber), var(--orange));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    filter: drop-shadow(0 0 20px rgba(245,158,11,0.6));
    position: relative;
    z-index: 1;
}

.kpi-unit {
    font-family: 'JetBrains Mono', monospace;
    font-size: 14px;
    color: rgba(245,158,11,0.6);
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-top: 6px;
    position: relative;
    z-index: 1;
}

.kpi-label {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 20px;
    font-weight: 600;
    color: var(--text-muted);
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-top: 8px;
    position: relative;
    z-index: 1;
}

/* ── STAT CARDS BELOW KPI ── */
.stat-card {
    background: rgba(245,158,11,0.05);
    border: 1px solid rgba(245,158,11,0.15);
    border-radius: 14px;
    padding: 18px;
    text-align: center;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.stat-card::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0;
    width: 100%; height: 3px;
    background: linear-gradient(90deg, var(--amber), var(--orange));
    transform: scaleX(0);
    transform-origin: left;
    transition: transform 0.3s ease;
}

.stat-card:hover::after { transform: scaleX(1); }

.stat-card:hover {
    border-color: rgba(245,158,11,0.35);
    transform: translateY(-3px);
    box-shadow: var(--glow);
}

.stat-val {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 28px;
    font-weight: 900;
    color: var(--amber);
}

.stat-lbl {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    color: var(--text-muted);
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-top: 4px;
}

/* ── ANALYTICS SECTION TITLE ── */
.section-title {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 18px;
    font-weight: 700;
    color: var(--amber);
    text-transform: uppercase;
    letter-spacing: 3px;
    padding-bottom: 10px;
    border-bottom: 1px solid rgba(245,158,11,0.12);
    margin: 28px 0 18px;
}

/* ── TABS ── */
.stTabs [data-baseweb="tab-list"] {
    background: rgba(245,158,11,0.04) !important;
    border-radius: 12px !important;
    border: 1px solid rgba(245,158,11,0.1) !important;
    padding: 5px !important;
    gap: 4px !important;
}

.stTabs [data-baseweb="tab"] {
    font-family: 'Barlow Condensed', sans-serif !important;
    font-size: 14px !important;
    font-weight: 700 !important;
    letter-spacing: 3px !important;
    text-transform: uppercase !important;
    color: rgba(245,158,11,0.55) !important;
    border-radius: 9px !important;
    padding: 10px 22px !important;
    transition: all 0.3s ease !important;
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, rgba(245,158,11,0.2), rgba(234,88,12,0.2)) !important;
    color: var(--amber) !important;
    box-shadow: 0 0 15px rgba(245,158,11,0.15) !important;
}

/* ── SIDEBAR ── */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0d0d0d 0%, #141414 100%) !important;
    border-right: 1px solid rgba(245,158,11,0.1) !important;
}

.sb-logo {
    text-align: center;
    padding: 10px 0 22px;
}

.sb-logo-text {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 28px;
    font-weight: 900;
    letter-spacing: 4px;
    text-transform: uppercase;
    background: linear-gradient(135deg, var(--amber), var(--orange));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.sb-logo-sub {
    font-family: 'JetBrains Mono', monospace;
    font-size: 9px;
    color: rgba(245,158,11,0.4);
    letter-spacing: 3px;
    margin-top: 3px;
}

.sb-info {
    background: rgba(245,158,11,0.05);
    border: 1px solid rgba(245,158,11,0.14);
    border-radius: 12px;
    padding: 16px;
    font-family: 'Exo 2', sans-serif;
    font-size: 14px;
    color: rgba(245,240,232,0.75);
    line-height: 1.9;
}

.sb-info span { color: var(--amber); font-weight: 700; }

.sb-title {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 13px;
    font-weight: 700;
    color: var(--amber);
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 10px;
}

/* ── METRIC CARD (sidebar) ── */
.sb-metric {
    background: rgba(245,158,11,0.05);
    border: 1px solid rgba(245,158,11,0.14);
    border-radius: 10px;
    padding: 14px;
    text-align: center;
}

.sb-metric-val {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 24px;
    font-weight: 900;
    color: var(--amber);
}

.sb-metric-lbl {
    font-family: 'JetBrains Mono', monospace;
    font-size: 9px;
    color: var(--text-muted);
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-top: 4px;
}

/* ── LIVE BADGE ── */
.live-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(16,185,129,0.08);
    border: 1px solid rgba(16,185,129,0.2);
    border-radius: 50px;
    padding: 8px 18px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    color: rgba(16,185,129,0.9);
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 22px;
}

.live-dot {
    width: 7px; height: 7px;
    border-radius: 50%;
    background: var(--green);
    box-shadow: 0 0 8px var(--green);
    animation: liveBlink 1.4s ease-in-out infinite;
}

@keyframes liveBlink {
    0%, 100% { opacity: 1; box-shadow: 0 0 8px var(--green); }
    50%       { opacity: 0.3; box-shadow: 0 0 3px var(--green); }
}

/* ── INSIGHT CARD (tab3) ── */
.insight-card {
    background: rgba(245,158,11,0.04);
    border: 1px solid rgba(245,158,11,0.13);
    border-left: 4px solid var(--amber);
    border-radius: 12px;
    padding: 18px 22px;
    margin-bottom: 14px;
    font-family: 'Exo 2', sans-serif;
    font-size: 15px;
    color: rgba(245,240,232,0.8);
    line-height: 1.7;
    transition: all 0.25s ease;
}

.insight-card:hover {
    background: rgba(245,158,11,0.08);
    border-left-color: var(--orange);
    transform: translateX(4px);
}

.insight-card b { color: var(--amber); }

/* ── PROGRESS BAR ── */
div[data-testid="stProgressBar"] > div {
    background: linear-gradient(90deg, var(--amber), var(--orange)) !important;
    border-radius: 99px !important;
}

div[data-testid="stProgressBar"] {
    background: rgba(245,158,11,0.1) !important;
    border-radius: 99px !important;
}

/* ── SCROLLBAR ── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: var(--dark-950); }
::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, var(--amber), var(--orange));
    border-radius: 3px;
}

/* ── INFO / SUCCESS BOX ── */
div[data-testid="stInfo"],
div[data-testid="stSuccess"] {
    background: rgba(245,158,11,0.05) !important;
    border: 1px solid rgba(245,158,11,0.2) !important;
    border-radius: 12px !important;
    font-family: 'Exo 2', sans-serif !important;
    color: rgba(245,240,232,0.8) !important;
}

/* ── FLOATING PARTICLES ── */
.particles {
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 0;
    overflow: hidden;
}

.pt {
    position: absolute;
    border-radius: 50%;
    animation: ptFloat linear infinite;
}

.pt:nth-child(1)  { width:2px; height:2px; left: 8%;  background:var(--amber); box-shadow:0 0 5px var(--amber); animation-duration:14s; animation-delay:0s;   opacity:0.5; }
.pt:nth-child(2)  { width:2px; height:2px; left:20%;  background:var(--orange);box-shadow:0 0 5px var(--orange);animation-duration:19s; animation-delay:3s;   opacity:0.4; }
.pt:nth-child(3)  { width:3px; height:3px; left:33%;  background:var(--amber); box-shadow:0 0 8px var(--amber); animation-duration:12s; animation-delay:6s;   opacity:0.6; }
.pt:nth-child(4)  { width:2px; height:2px; left:50%;  background:var(--green); box-shadow:0 0 5px var(--green); animation-duration:22s; animation-delay:1s;   opacity:0.3; }
.pt:nth-child(5)  { width:2px; height:2px; left:65%;  background:var(--amber); box-shadow:0 0 5px var(--amber); animation-duration:16s; animation-delay:8s;   opacity:0.5; }
.pt:nth-child(6)  { width:2px; height:2px; left:78%;  background:var(--orange);box-shadow:0 0 5px var(--orange);animation-duration:20s; animation-delay:4s;   opacity:0.4; }
.pt:nth-child(7)  { width:3px; height:3px; left:88%;  background:var(--amber); box-shadow:0 0 8px var(--amber); animation-duration:15s; animation-delay:2s;   opacity:0.6; }
.pt:nth-child(8)  { width:2px; height:2px; left:95%;  background:var(--green); box-shadow:0 0 5px var(--green); animation-duration:18s; animation-delay:7s;   opacity:0.3; }

@keyframes ptFloat {
    0%   { transform: translateY(110vh) scale(0);   opacity: 0; }
    10%  { opacity: 0.7; }
    90%  { opacity: 0.5; }
    100% { transform: translateY(-10vh) scale(1.5); opacity: 0; }
}

/* ── FOOTER ── */
.footer {
    text-align: center;
    padding: 28px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    color: rgba(245,158,11,0.3);
    letter-spacing: 2px;
    text-transform: uppercase;
    border-top: 1px solid rgba(245,158,11,0.08);
    margin-top: 40px;
    position: relative;
    z-index: 1;
}
</style>

<!-- Floating Particles -->
<div class="particles">
    <div class="pt"></div><div class="pt"></div><div class="pt"></div>
    <div class="pt"></div><div class="pt"></div><div class="pt"></div>
    <div class="pt"></div><div class="pt"></div>
</div>
""",
    unsafe_allow_html=True,
)

# ============================================================
# SESSION STATE INIT
# ============================================================
for _key in ("predicted_time", "distance", "prep_time", "weather", "traffic", "vehicle"):
    if _key not in st.session_state:
        st.session_state[_key] = None

# ============================================================
# SIDEBAR
# ============================================================
with st.sidebar:

    st.markdown(
        """
        <div class="sb-logo">
            <div class="sb-logo-text">DTIS</div>
            <div class="sb-logo-sub">Delivery Time Intelligence</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="sb-title">&#128230; System Overview</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="sb-info">
            <span>Algorithm:</span> Linear Regression<br>
            <span>Encoding:</span> One-Hot Encoding<br>
            <span>Features:</span> 7 Input Variables<br>
            <span>Task:</span> Continuous Time Prediction<br>
            <span>Deployment:</span> Streamlit Enterprise
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="sb-title">&#128202; Model Metrics</div>', unsafe_allow_html=True)

    sb_c1, sb_c2 = st.columns(2)
    with sb_c1:
        st.markdown(
            """<div class="sb-metric">
                <div class="sb-metric-val">LR</div>
                <div class="sb-metric-lbl">Algorithm</div>
            </div>""",
            unsafe_allow_html=True,
        )
    with sb_c2:
        st.markdown(
            """<div class="sb-metric">
                <div class="sb-metric-val">7</div>
                <div class="sb-metric-lbl">Features</div>
            </div>""",
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # Live result in sidebar
    st.markdown('<div class="sb-title">&#9201; Live Prediction</div>', unsafe_allow_html=True)

    if st.session_state.predicted_time is not None:
        pt   = st.session_state.predicted_time
        frac = min(float(pt) / 120.0, 1.0)
        color = "#10b981" if pt <= 30 else ("#f59e0b" if pt <= 60 else "#ef4444")
        st.markdown(
            f"""
            <div style='background:rgba(0,0,0,0.4); border:1px solid {color}44;
                        border-radius:14px; padding:18px; text-align:center;
                        box-shadow: 0 0 20px {color}22;'>
                <div style='font-family:"Barlow Condensed",sans-serif; font-size:42px;
                            font-weight:900; color:{color};
                            text-shadow: 0 0 20px {color};'>{pt}</div>
                <div style='font-family:"JetBrains Mono",monospace; font-size:10px;
                            color:rgba(255,255,255,0.45); letter-spacing:2px; margin-top:4px;'>
                    MINUTES
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.progress(frac)
    else:
        st.markdown(
            """<div style='background:rgba(245,158,11,0.03); border:1px solid rgba(245,158,11,0.1);
                           border-radius:14px; padding:18px; text-align:center;'>
                <div style='font-family:"JetBrains Mono",monospace; font-size:10px;
                            color:rgba(245,158,11,0.4); letter-spacing:2px;'>AWAITING INPUT</div>
            </div>""",
            unsafe_allow_html=True,
        )
        st.progress(0.0)

    st.markdown("<br>", unsafe_allow_html=True)
    with st.expander("&#9881;&#65039; How It Works"):
        st.markdown(
            """<div style='font-family:"Exo 2",sans-serif; font-size:13px;
                           color:rgba(245,240,232,0.7); line-height:1.85;'>
                1. Enter order &amp; route details<br>
                2. One-hot encoding applied<br>
                3. Linear Regression predicts time<br>
                4. Analytics reveal key drivers<br>
                5. Use insights to optimise logistics
            </div>""",
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        """<div style='background:linear-gradient(135deg,rgba(245,158,11,0.12),rgba(234,88,12,0.12));
                       border:1px solid rgba(245,158,11,0.2); border-radius:12px;
                       padding:14px; text-align:center;'>
            <div style='font-family:"Barlow Condensed",sans-serif; font-size:12px;
                        font-weight:700; color:var(--amber); letter-spacing:2px;'>
                &#128640; ENTERPRISE LOGISTICS AI
            </div>
            <div style='font-family:"JetBrains Mono",monospace; font-size:9px;
                        color:rgba(255,255,255,0.3); letter-spacing:1px; margin-top:6px;'>
                Developed by Akshit Gajera
            </div>
        </div>""",
        unsafe_allow_html=True,
    )

# ============================================================
# HERO HEADER
# ============================================================
st.markdown(
    """
    <div class="hero-wrap">
        <div class="hero-eyebrow">&#9888; Enterprise Logistics Intelligence Platform</div>
        <div class="hero-title">Delivery Time <span>Intelligence</span></div>
        <div class="hero-sub">AI-Powered Route &amp; Time Optimisation System</div>
        <div class="hero-divider">
            <div class="hero-divider-line"></div>
            <div class="hero-divider-diamond"></div>
            <div class="hero-divider-line"></div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Animated ticker bar
ticker_content = (
    '<span class="ticker-item"><span class="ticker-dot"></span>LINEAR REGRESSION MODEL</span>'
    '<span class="ticker-item"><span class="ticker-dot"></span>ONE-HOT ENCODING</span>'
    '<span class="ticker-item"><span class="ticker-dot"></span>7 FEATURE INPUTS</span>'
    '<span class="ticker-item"><span class="ticker-dot"></span>REAL-TIME PREDICTION</span>'
    '<span class="ticker-item"><span class="ticker-dot"></span>ROUTE ANALYTICS</span>'
    '<span class="ticker-item"><span class="ticker-dot"></span>ENTERPRISE GRADE</span>'
)
# Duplicate for seamless loop
st.markdown(
    f'<div class="ticker-bar"><div class="ticker-inner">{ticker_content}{ticker_content}</div></div>',
    unsafe_allow_html=True,
)

# ============================================================
# TABS
# ============================================================
tab1, tab2, tab3 = st.tabs(
    ["&#9889;  PREDICTION ENGINE", "&#128202;  ANALYTICS SUITE", "&#129504;  MODEL INSIGHTS"]
)

# ============================================================
# TAB 1 — PREDICTION ENGINE
# ============================================================
with tab1:

    st.markdown(
        """<div class="glass-panel">
            <div class="panel-label">Order Configuration</div>
            <div class="panel-title">Enter Delivery Parameters</div>
        </div>""",
        unsafe_allow_html=True,
    )

    # Live badge
    st.markdown(
        '<div class="live-badge"><div class="live-dot"></div>Model Ready — Enter Parameters Below</div>',
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="input-group-label">&#128205; Route Details</div>', unsafe_allow_html=True)
        distance    = st.number_input("Distance (km)",                min_value=0.0,  max_value=100.0, value=5.0,  step=0.5)
        weather     = st.selectbox("Weather Condition",               ["Sunny", "Rainy", "Foggy", "Stormy"])

    with col2:
        st.markdown('<div class="input-group-label">&#128341; Time &amp; Traffic</div>', unsafe_allow_html=True)
        traffic     = st.selectbox("Traffic Level",                   ["Low", "Medium", "High"])
        time_of_day = st.selectbox("Time of Day",                     ["Morning", "Afternoon", "Evening", "Night"])

    with col3:
        st.markdown('<div class="input-group-label">&#128666; Vehicle &amp; Prep</div>', unsafe_allow_html=True)
        vehicle     = st.selectbox("Vehicle Type",                    ["Bike", "Scooter", "Car"])
        prep_time   = st.number_input("Preparation Time (minutes)",   min_value=0,    max_value=120,   value=15)

    st.markdown("<br>", unsafe_allow_html=True)
    exp_col, _ = st.columns([1, 2])
    with exp_col:
        experience = st.number_input(
            "Courier Experience (years)", min_value=0, max_value=20, value=2
        )

    st.markdown("<br>", unsafe_allow_html=True)
    _, btn_col, _ = st.columns([1, 2, 1])
    with btn_col:
        predict_clicked = st.button("&#128269;  CALCULATE DELIVERY TIME", use_container_width=True)

    # ── Run Prediction ──
    if predict_clicked:
        input_df = pd.DataFrame(
            {
                "Distance_km":            [distance],
                "Weather":                [weather],
                "Traffic_Level":          [traffic],
                "Time_of_Day":            [time_of_day],
                "Vehicle_Type":           [vehicle],
                "Preparation_Time_min":   [prep_time],
                "Courier_Experience_yrs": [experience],
            }
        )
        input_encoded = pd.get_dummies(input_df)
        input_encoded = input_encoded.reindex(columns=dummy_columns, fill_value=0)

        raw_pred = model.predict(input_encoded)
        predicted_time = round(float(raw_pred[0]), 2)

        # Persist in session state
        st.session_state.predicted_time = predicted_time
        st.session_state.distance       = float(distance)
        st.session_state.prep_time      = float(prep_time)
        st.session_state.weather        = weather
        st.session_state.traffic        = traffic
        st.session_state.vehicle        = vehicle

    # ── Display Result ──
    if st.session_state.predicted_time is not None:
        pt = st.session_state.predicted_time

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(
            f"""
            <div class="kpi-box">
                <div class="kpi-value">{pt}</div>
                <div class="kpi-unit">Minutes</div>
                <div class="kpi-label">Estimated Delivery Time</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # ── Quick stat chips ──
        st.markdown("<br>", unsafe_allow_html=True)
        sc1, sc2, sc3, sc4 = st.columns(4)
        d_val  = st.session_state.distance   if st.session_state.distance   is not None else distance
        p_val  = st.session_state.prep_time  if st.session_state.prep_time  is not None else prep_time
        w_val  = st.session_state.weather    if st.session_state.weather    is not None else weather
        v_val  = st.session_state.vehicle    if st.session_state.vehicle    is not None else vehicle

        chips = [
            (f"{d_val} km",   "Distance"),
            (f"{p_val} min",  "Prep Time"),
            (str(w_val),      "Weather"),
            (str(v_val),      "Vehicle"),
        ]
        for col, (val, lbl) in zip([sc1, sc2, sc3, sc4], chips):
            with col:
                st.markdown(
                    f"""<div class="stat-card">
                        <div class="stat-val">{val}</div>
                        <div class="stat-lbl">{lbl}</div>
                    </div>""",
                    unsafe_allow_html=True,
                )

# ============================================================
# TAB 2 — ANALYTICS SUITE
# ============================================================
with tab2:

    if st.session_state.predicted_time is None:
        st.markdown(
            """<div style='text-align:center; padding:80px 20px; font-family:"Barlow Condensed",sans-serif;
                           font-size:18px; letter-spacing:3px; text-transform:uppercase;
                           color:rgba(245,158,11,0.4);'>
                &#9672; Run Prediction First To Unlock Analytics &#9672;
            </div>""",
            unsafe_allow_html=True,
        )
    else:
        base_time = float(st.session_state.predicted_time)
        base_dist = float(st.session_state.distance) if st.session_state.distance else 5.0
        base_prep = float(st.session_state.prep_time) if st.session_state.prep_time else 15.0

        # Guard: avoid division by zero
        if base_dist == 0:
            base_dist = 1.0

        # ── Distance vs Time Simulation ──
        st.markdown('<div class="section-title">&#128205; Distance vs Delivery Time Simulation</div>', unsafe_allow_html=True)

        sim_distances = np.linspace(1.0, 30.0, 30).tolist()
        sim_times     = [round(base_time * (d / base_dist), 2) for d in sim_distances]

        fig_dist = go.Figure()
        fig_dist.add_trace(
            go.Scatter(
                x=sim_distances,
                y=sim_times,
                mode="lines+markers",
                line=dict(color="#f59e0b", width=3, shape="spline"),
                marker=dict(color="#ea580c", size=7, line=dict(color="#f59e0b", width=2)),
                fill="tozeroy",
                fillcolor="rgba(245,158,11,0.07)",
                name="Estimated Time",
            )
        )
        # Mark current distance
        fig_dist.add_vline(
            x=base_dist,
            line=dict(color="#ea580c", width=2, dash="dash"),
            annotation_text=f"Current: {base_dist} km",
            annotation_font_color="#ea580c",
        )
        fig_dist.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(245,158,11,0.02)",
            font=dict(family="Exo 2", color="#f59e0b"),
            xaxis=dict(
                title="Distance (km)",
                gridcolor="rgba(245,158,11,0.08)",
                color="rgba(245,158,11,0.7)",
            ),
            yaxis=dict(
                title="Estimated Time (min)",
                gridcolor="rgba(245,158,11,0.08)",
                color="rgba(245,158,11,0.7)",
            ),
            height=360,
            margin=dict(l=20, r=20, t=20, b=20),
            showlegend=False,
        )
        st.plotly_chart(fig_dist, use_container_width=True)

        # ── Preparation Time Impact ──
        st.markdown('<div class="section-title">&#9201; Preparation Time Sensitivity</div>', unsafe_allow_html=True)

        prep_range  = np.linspace(5.0, 60.0, 30).tolist()
        prep_effect = [round(base_time + (p - base_prep), 2) for p in prep_range]

        fig_prep = go.Figure()
        fig_prep.add_trace(
            go.Scatter(
                x=prep_range,
                y=prep_effect,
                mode="lines+markers",
                line=dict(color="#ea580c", width=3, shape="spline"),
                marker=dict(color="#f59e0b", size=7, line=dict(color="#ea580c", width=2)),
                fill="tozeroy",
                fillcolor="rgba(234,88,12,0.07)",
                name="Time Impact",
            )
        )
        fig_prep.add_vline(
            x=base_prep,
            line=dict(color="#f59e0b", width=2, dash="dash"),
            annotation_text=f"Current: {base_prep} min",
            annotation_font_color="#f59e0b",
        )
        fig_prep.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(234,88,12,0.02)",
            font=dict(family="Exo 2", color="#f59e0b"),
            xaxis=dict(
                title="Preparation Time (min)",
                gridcolor="rgba(245,158,11,0.08)",
                color="rgba(245,158,11,0.7)",
            ),
            yaxis=dict(
                title="Estimated Delivery Time (min)",
                gridcolor="rgba(245,158,11,0.08)",
                color="rgba(245,158,11,0.7)",
            ),
            height=360,
            margin=dict(l=20, r=20, t=20, b=20),
            showlegend=False,
        )
        st.plotly_chart(fig_prep, use_container_width=True)

        # ── Traffic Scenario Bar ──
        st.markdown('<div class="section-title">&#128656; Traffic Level Impact (Simulated)</div>', unsafe_allow_html=True)

        traffic_multipliers = {"Low": 0.85, "Medium": 1.0, "High": 1.25}
        traffic_labels      = list(traffic_multipliers.keys())
        traffic_times       = [round(base_time * m, 2) for m in traffic_multipliers.values()]
        bar_colors          = ["rgba(16,185,129,0.7)", "rgba(245,158,11,0.7)", "rgba(239,68,68,0.7)"]
        border_colors       = ["#10b981", "#f59e0b", "#ef4444"]

        fig_traffic = go.Figure()
        fig_traffic.add_trace(
            go.Bar(
                x=traffic_labels,
                y=traffic_times,
                marker=dict(
                    color=bar_colors,
                    line=dict(color=border_colors, width=2),
                ),
                text=[f"{t} min" for t in traffic_times],
                textposition="outside",
                textfont=dict(family="Barlow Condensed", size=14, color="white"),
            )
        )
        fig_traffic.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(245,158,11,0.02)",
            font=dict(family="Exo 2", color="#f59e0b"),
            xaxis=dict(gridcolor="rgba(245,158,11,0.08)", color="rgba(245,158,11,0.7)"),
            yaxis=dict(
                title="Estimated Time (min)",
                gridcolor="rgba(245,158,11,0.08)",
                color="rgba(245,158,11,0.7)",
            ),
            height=340,
            margin=dict(l=20, r=20, t=30, b=20),
            showlegend=False,
        )
        st.plotly_chart(fig_traffic, use_container_width=True)

# ============================================================
# TAB 3 — MODEL INSIGHTS
# ============================================================
with tab3:

    st.markdown('<div class="section-title">&#129504; Why Linear Regression?</div>', unsafe_allow_html=True)

    insights_why = [
        ("<b>Interpretable coefficients</b> — each feature's weight directly explains its effect on delivery time.",),
        ("<b>Fast inference</b> — predictions computed in milliseconds, ideal for real-time logistics.",),
        ("<b>Continuous output</b> — naturally suited for time prediction (a regression target).",),
        ("<b>Seamless OHE integration</b> — one-hot encoding converts categoricals to numeric with no information loss.",),
    ]
    for (text,) in insights_why:
        st.markdown(f'<div class="insight-card">{text}</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">&#128204; Key Business Insights</div>', unsafe_allow_html=True)

    insights_biz = [
        ("<b>Distance</b> is the single strongest driver of delivery time — optimise routing to reduce km.",),
        ("<b>Preparation time</b> adds directly to total time — kitchen efficiency is critical.",),
        ("<b>Traffic conditions</b> introduce variance — consider off-peak delivery incentives.",),
        ("<b>Courier experience</b> reduces delay risk — experienced riders navigate faster.",),
        ("<b>Vehicle type</b> impacts speed on different road types — match vehicle to route profile.",),
        ("<b>Weather</b> degrades performance in Rainy/Stormy conditions — add buffer time estimates.",),
    ]
    for (text,) in insights_biz:
        st.markdown(f'<div class="insight-card">{text}</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">&#128200; Feature Overview</div>', unsafe_allow_html=True)

    feature_data = {
        "Feature":      ["Distance_km", "Weather", "Traffic_Level", "Time_of_Day", "Vehicle_Type", "Preparation_Time_min", "Courier_Experience_yrs"],
        "Type":         ["Numeric", "Categorical", "Categorical", "Categorical", "Categorical", "Numeric", "Numeric"],
        "Encoding":     ["None", "One-Hot", "One-Hot", "One-Hot", "One-Hot", "None", "None"],
        "Impact Level": ["High", "Medium", "High", "Low", "Medium", "High", "Medium"],
    }
    feat_df = pd.DataFrame(feature_data)
    st.dataframe(feat_df, use_container_width=True, hide_index=True)

# ============================================================
# FOOTER
# ============================================================
st.markdown(
    """
    <div class="footer">
        &copy; 2026 &nbsp;|&nbsp; Akshit Gajera &nbsp;|&nbsp;
        Delivery Time Intelligence Platform &nbsp;|&nbsp;
        Linear Regression &nbsp;|&nbsp; Enterprise Logistics AI
    </div>
    """,
    unsafe_allow_html=True,
)
