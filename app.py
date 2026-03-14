import streamlit as st
import cv2
from ultralytics import YOLO
import yt_dlp
import datetime
import time

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="MONITORING - D_ONEJECT", layout="wide")

# CSS untuk Custom Styling agar mirip UI yang kamu kirim
st.markdown("""
    <style>
    .main { background-color: #000000; color: #ffffff; }
    .stButton>button { width: 100%; background-color: #0e4b61; color: white; border-radius: 20px; border: 1px solid #58a6ff; }
    .metric-card { background-color: #161b22; border: 1px solid #30363d; padding: 15px; border-radius: 10px; text-align: center; }
    .digital-clock { font-family: 'Courier New', Courier, monospace; color: #58a6ff; font-size: 40px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (MENU KIRI) ---
with st.sidebar:
    st.title("D_ONEJECT")
    st.markdown("---")
    menu = st.radio("MENU UTAMA", ["PILIH KAMERA", "PUTAR ULANG", "OUTPUT DATA", "GRAFIK", "DESKRIPSI LAPORAN", "INFORMASI"])
    st.markdown("---")
    if st.button("Exit / Logout"):
        st.write("Logged out")

# --- HEADER (JAM & TANGGAL) ---
col_t1, col_t2, col_t3 = st.columns([2, 1, 1])
with col_t1:
    st.markdown(f"<div class='digital-clock'>{datetime.datetime.now().strftime('%H:%M:%S %p')}</div>", unsafe_allow_html=True)
with col_t2:
    st.subheader(datetime.datetime.now().strftime("%d-%B-%Y"))
with col_t3:
    st.markdown("<div class='metric-card'>SHIFT<br><h2>1</h2></div>", unsafe_allow_html=True)

# --- AREA MONITORING ---
if menu == "PILIH KAMERA":
    # Database CCTV (Bisa kamu tambah lagi sesuai list sebelumnya)
    cctv_list = {
        "Simpang Tugu": "https://www.youtube.com/live/1v52cQ1qJBA",
        "Nol KM": "https://www.youtube.com/live/n7FLPsRLboI",
        "Malioboro": "https://www.youtube.com/live/cabN74Gdbc8"
    }
    
    selected_cctv = st.selectbox("Pilih Lokasi Kamera", list(cctv_list.keys()))
    
    col_v1, col_v2 = st.columns([3, 1])
    
    with col_v1:
        st.markdown(f"### Live Feed: {selected_cctv}")
        # Placeholder untuk Video
        video_placeholder = st.empty()
        # Tombol Jalankan AI
        if st.button("Mulai Analisis AI"):
            # Logika deteksi YOLO di sini (Running di loop)
            st.warning("Fitur deteksi sedang diproses... (Gunakan Streamlit WebRTC untuk performa lebih baik di web)")

    with col_v2:
        st.markdown("<div class='metric-card'>KECEPATAN RATA-RATA<br><h3>40 KM/JAM</h3></div>", unsafe_allow_html=True)
        st.markdown("---")
        # Widget Jumlah Kendaraan (Sesuai Gambar 1)
        st.write("📊 Statistik Real-time")
        st.metric("MOBIL PRIBADI", "00000")
        st.metric("SEPEDA MOTOR", "00000")
        st.metric("MOBIL BARANG", "00000")

elif menu == "GRAFIK":
    st.header("Grafik Aktivitas Kendaraan")
    col_g1, col_g2 = st.columns(2)
    with col_g1:
        st.write("KENDARAAN KE TIMUR")
        # Contoh Pie Chart
        st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=100) # Ganti dengan chart asli
    with col_g2:
        st.write("KENDARAAN KE BARAT")
