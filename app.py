import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="SISMONRAN 1.0 - Monitoring", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    [data-testid="stSidebar"] { background-color: #222d32; color: white; }
    [data-testid="stSidebar"] .stMarkdown p { color: #b8c7ce; }
    .stMetric { background-color: #ffffff; border-top: 3px solid #00c0ef; padding: 15px; border-radius: 5px; box-shadow: 0 1px 1px rgba(0,0,0,0.1); }
    .main-header { font-size: 24px; font-weight: bold; margin-bottom: -10px; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (NAVIGASI) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=70)
    st.markdown("**DZAKWAN DHIHA MUHADZDZIB** \n*Admin Utama*")
    st.markdown("---")
    st.markdown("🔍 **Navigation**")
    menu = st.radio("", ["Dashboard", "Master Setup", "Master Kendaraan", "Rekapitulasi"])
    st.markdown("---")
    st.info("Sistem Monitoring Aktif")

# --- MAIN CONTENT ---
st.markdown('<p class="main-header">Dashboard <span style="font-weight:normal; font-size:16px; color:#999;">Overview & statistic</span></p>', unsafe_allow_html=True)

# Banner Hijau Welcome - NAMA DIGANTI SISMONRAN
st.success("✅ **Welcome To SISMONRAN Version 1.0**. Aplikasi Sistem Informasi Monitoring Arus Lalu Lintas Pintar.")

# --- BARIS 1: KARTU STATISTIK ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="TOTAL KENDARAAN", value="1,245", delta="Real-time")
with col2:
    st.metric(label="RATA2 KECEPATAN", value="45 km/jam", delta="Lancar")
with col3:
    st.metric(label="KEMACETAN", value="15%", delta="Rendah")
with col4:
    st.metric(label="PELANGGARAN", value="12", delta="CCTV Aktif")

st.markdown("---")

# --- BARIS 2: TABEL & GRAFIK ---
col_table, col_chart = st.columns([1, 1])

with col_table:
    st.markdown("
