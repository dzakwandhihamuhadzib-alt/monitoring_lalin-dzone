import streamlit as st
import cv2
from ultralytics import YOLO
import yt_dlp
import datetime
import pandas as pd
import plotly.express as px
import time

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="MONITORING - D_ONEJECT", layout="wide", initial_sidebar_state="expanded")

# --- CSS UNTUK REPLIKASI DESAIN PERSIS ---
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] { 
        background-color: #161b22; 
        border-right: 1px solid #30363d; 
    }
    
    /* Navigasi Tombol Sidebar */
    .stButton>button {
        width: 100%;
        background-color: #0b3d51;
        color: #ffffff;
        border-radius: 15px;
        border: 1px solid #58a6ff;
        font-weight: bold;
        margin-bottom: -10px;
        height: 45px;
    }
    .stButton>button:hover { background-color: #1a6a8a; border-color: white; }

    /* Jam Digital Besar (Header) */
    .digital-clock {
        background-color: #0d1117;
        border: 2px solid #58a6ff;
        padding: 15px;
        border-radius: 10px;
        color: #58a6ff;
        font-family: 'Courier New', monospace;
        font-size: 55px;
        text-align: center;
        box-shadow: 0 0 20px rgba(88, 166, 255, 0.4);
    }

    /* Widget Box (Kecepatan & Shift) */
    .widget-box {
        background-color: #24343d;
        border: 1px solid #30363d;
        padding: 15px;
        border-radius: 15px;
        text-align: center;
        height: 140px;
    }
    .widget-title { font-size: 14px; color: #c9d1d9; text-transform: uppercase; }
    .widget-value { font-size: 40px; font-weight: bold; color: #58a6ff; font-family: 'Courier New', monospace; }

    /* Kotak Statistik Kendaraan (Bawah) */
    .stat-box {
        background-color: #24343d;
        border: 1px solid #30363d;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        min-height: 100px;
    }
    .stat-label { font-size: 11px; color: #c9d1d9; margin-bottom: 5px; }
    .stat-number { font-size: 24px; color: #58a6ff; font-family: 'Courier New', monospace; letter-spacing: 3px; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (NAVIGASI GAMBAR 1-7) ---
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #58a6ff; margin-bottom:0;'>MONITORING</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; margin-top: -10px;'>D_ONEJECT</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("PILIH KAMERA"): st.session_state.menu = "kamera"
    if st.button("DATA PER JAM"): st.session_state.menu = "data_jam"
    if st.button("OUTPUT DATA"): st.session_state.menu = "data"
    if st.button("GRAFIK"): st.session_state.menu = "grafik"
    if st.button("DESKRIPSI LAPORAN"): st.session_state.menu = "laporan"
    if st.button("INFORMASI"): st.session_state.menu = "info"
    
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("<hr style='border-top: 1px solid #30363d;'>", unsafe_allow_html=True)
    if st.button("🚪 Exit / Logout"): st.stop()

# Default Menu
if 'menu' not in st.session_state: st.session_state.menu = "kamera"

# --- HEADER (JAM & WIDGET UTAMA) ---
col_h1, col_h2, col_h3, col_h4 = st.columns([2.5, 1.5, 1.5, 1])

with col_h1:
    st.markdown(f"<div class='digital-clock'>{datetime.datetime.now().strftime('%H:%M:%S %p')}</div>", unsafe_allow_html=True)

with col_h2:
    st.markdown(f"<div style='text-align:center; padding-top:20px;'><h3>{datetime.datetime.now().strftime('%d-%B-%Y')}</h3></div>", unsafe_allow_html=True)

with col_h3:
    st.markdown("<div class='widget-box'><span class='widget-title'>KECEPATAN RATA-RATA</span><br>KENDARAAN<br><span class='widget-value'>040 KM/JAM</span></div>", unsafe_allow_html=True)

with col_h4:
    st.markdown("<div class='widget-box'><span class='widget-title'>SHIFT</span><br><br><span class='widget-value' style='font-size:60px'>1</span></div>", unsafe_allow_html=True)

st.markdown("<hr style='border-top: 2px solid #ffffff; margin: 10px 0;'>", unsafe_allow_html=True)

# --- LOGIKA TAMPILAN PER MENU ---

# 1. MENU PILIH KAMERA (Sesuai Video & Gambar 1-2)
if st.session_state.menu == "kamera":
    # Monitor Utama
    st.markdown("<div style='background-color:#0b3d51; height:400px; border-radius:20px; border:1px solid #58a6ff; display:flex; align-items:center; justify-content:center; margin-bottom:20px;'><h2>LAYAR MONITOR UTAMA</h2></div>", unsafe_allow_html=True)
    
    # Statistik Bawah (Grid 5 Kolom - Ke Timur & Ke Barat)
    def stat_row(label):
        st.markdown(f"<p style='text-align:right; font-weight:bold; margin-bottom:5px; color:#58a6ff;'>{label}</p>", unsafe_allow_html=True)
        cols = st.columns(5)
        categories = ["AKAP / BUS / PARIWISATA / TAXI / SHUTTLE", "AKDP / PERDESAAN", "MOBIL PRIBADI", "MOBIL BARANG", "SEPEDA MOTOR"]
        for i, cat in enumerate(categories):
            with cols[i]:
                st.markdown(f"<div class='stat-box'><div class='stat-label'>{cat}</div><div class='stat-number'>00000</div></div>", unsafe_allow_html=True)

    stat_row("KE TIMUR")
    st.markdown("<br>", unsafe_allow_html=True)
    stat_row("KE BARAT")

# 2. MENU GRAFIK (Sesuai Gambar 5)
elif st.session_state.menu == "grafik":
    st.markdown("<h2 style='text-align:center;'>REKAPITULASI DATA KENDARAAN</h2>", unsafe_allow_html=True)
    
    data = {"Kategori": ["Sepeda Motor", "Mobil Pribadi", "Mobil Barang", "AKAP/Bus"], "Persen": [50.06, 39.43, 7.50, 3.01]}
    df = pd.DataFrame(data)
    
    cg1, cg2 = st.columns(2)
    with cg1:
        st.markdown("<h3 style='text-align:center;'>KENDARAAN KE TIMUR</h3>", unsafe_allow_html=True)
        fig1 = px.pie(df, values='Persen', names='Kategori', hole=0.4, color_discrete_sequence=px.colors.sequential.RdBu)
        st.plotly_chart(fig1, use_container_width=True)
    with cg2:
        st.markdown("<h3 style='text-align:center;'>KENDARAAN KE BARAT</h3>", unsafe_allow_html=True)
        fig2 = px.pie(df, values='Persen', names='Kategori', hole=0.4, color_discrete_sequence=px.colors.sequential.Blues_r)
        st.plotly_chart(fig2, use_container_width=True)

# 3. MENU OUTPUT DATA (Sesuai Gambar 4)
elif st.session_state.menu == "data":
    st.markdown("<h2 style='text-align:center;'>JUMLAH KENDARAAN DALAM HARI</h2>", unsafe_allow_html=True)
    # Simulasi Tabel Rekapitulasi (Gambar 4)
    st.table(pd.DataFrame({
        "ARAH": ["KE TIMUR", "KE BARAT"],
        "AKAP/BUS": [27, 24],
        "AKDP": [12, 15],
        "PRIBADI": [355, 340],
        "BARANG": [68, 70],
        "MOTOR": [452, 448],
        "TOTAL": [914, 897]
    }))
    st.button("📥 DOWNLOAD REPORT (EXCEL)")

# 4. MENU INFORMASI (Sesuai Gambar 7)
elif st.session_state.menu == "info":
    st.markdown("<h1 style='text-align:center;'>ℹ️</h1>", unsafe_allow_html=True)
    for _ in range(4):
        st.markdown("<div style='background-color:white; height:80px; border-radius:15px; margin-bottom:15px;'></div>", unsafe_allow_html=True)
