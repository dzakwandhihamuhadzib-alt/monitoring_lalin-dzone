import streamlit as st
import pandas as pd
import plotly.express as px
import datetime

# Konfigurasi Halaman
st.set_page_config(page_title="Trafik-Watch AI", layout="wide")

# --- SIDEBAR MENU ---
st.sidebar.title("🚀 TRAFIK-WATCH v1.0")
st.sidebar.markdown("---")
menu = st.sidebar.selectbox("Pilih Navigasi:", 
    ["Dashboard Utama", "Live Monitoring", "Statistik Kendaraan", "Laporan Pelanggaran"])

st.sidebar.info("Login as: Indra Adikusuma (Admin)")

# --- LOGIK HALAMAN ---
if menu == "Dashboard Utama":
    st.header("📊 Dashboard Monitoring Arus Lalu Lintas")
    
    # Baris 1: Kartu Statistik (Metrics)
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Kendaraan", "1,234", "+5%")
    col2.metric("Rata-rata Kecepatan", "52 km/h", "-2 km/h")
    col3.metric("Sepeda Motor", "678")
    col4.metric("Mobil Pribadi", "410")

    st.markdown("---")

    # Baris 2: Grafik dan Tabel
    left_column, right_column = st.columns([2, 1])

    with left_column:
        st.subheader("📈 Tren Arus Kendaraan (Per Jam)")
        # Contoh data dummy untuk grafik
        chart_data = pd.DataFrame({
            'Jam': ['06:00', '08:00', '10:00', '12:00', '14:00', '16:00'],
            'Jumlah': [150, 450, 300, 250, 280, 580]
        })
        fig = px.line(chart_data, x='Jam', y='Jumlah', markers=True)
        st.plotly_chart(fig, use_container_width=True)

    with right_column:
        st.subheader("🚗 Komposisi Jenis")
        pie_data = pd.DataFrame({
            'Jenis': ['Motor', 'Mobil', 'Truk', 'Bis'],
            'Jumlah': [678, 410, 100, 46]
        })
        fig_pie = px.pie(pie_data, values='Jumlah', names='Jenis', hole=0.4)
        st.plotly_chart(fig_pie, use_container_width=True)

    # Baris 3: Tabel Log
    st.subheader("📋 Log Kendaraan Terakhir")
    log_data = pd.DataFrame({
        'Waktu': ['10:35:12', '10:35:10', '10:35:05', '10:35:01'],
        'Jenis': ['Sepeda Motor', 'Mobil', 'Truk', 'Bis'],
        'Kecepatan': ['48 km/h', '55 km/h', '32 km/h', '38 km/h'],
        'Status': ['Normal', 'Normal', 'Lambat', 'Normal']
    })
    st.table(log_data)

elif menu == "Live Monitoring":
    st.header("📹 Live AI Camera Feed")
    st.warning("Menghubungkan ke Kamera CCTV... (Simulasi)")
    # Di sini nanti tempat menaruh OpenCV Video Stream
    st.image("https://via.placeholder.com/800x450.png?text=Live+Camera+Detection+Feed", caption="Kamera 01 - Jl. Slamet Riyadi")
