import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="SISMAKADIS 1.0 - Monitoring", layout="wide")

# --- CUSTOM CSS (Agar Mirip Screenshot) ---
st.markdown("""
    <style>
    /* Mengubah warna Sidebar jadi Gelap */
    [data-testid="stSidebar"] {
        background-color: #222d32;
        color: white;
    }
    /* Warna teks menu sidebar */
    [data-testid="stSidebar"] .stMarkdown p {
        color: #b8c7ce;
    }
    /* Mengatur Card Statistik */
    .stMetric {
        background-color: #ffffff;
        border-top: 3px solid #00c0ef; /* Warna biru atas card */
        padding: 15px;
        border-radius: 5px;
        box-shadow: 0 1px 1px rgba(0,0,0,0.1);
    }
    /* Styling Header Dashboard */
    .main-header {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: -10px;
    }
    .sub-header {
        color: #666;
        font-size: 14px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (NAVIGASI) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=70) # Foto profil admin
    st.markdown("**Indra Adikusuma** \n*Admin*")
    st.markdown("---")
    
    st.markdown("🔍 **Navigation**")
    menu = st.radio("", ["Dashboard", "Master Setup", "Master Kendaraan", "Rekapitulasi", "Report", "Backup Database"])
    
    st.markdown("---")
    if st.button("Collapse"):
        st.write("Sidebar Collapsed")

# --- MAIN CONTENT ---
st.markdown('<p class="main-header">Dashboard <span style="font-weight:normal; font-size:16px; color:#999;">Overview & statistic</span></p>', unsafe_allow_html=True)

# Banner Hijau Welcome
st.success("✅ **Welcome To SISMAKADIS Version 1.0**. Aplikasi Sistem Informasi Monitoring Arus Lalu Lintas Pintar.")

# --- BARIS 1: KARTU STATISTIK (4 Kolom) ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="TOTAL KENDARAAN", value="1,245", delta="Mobil & Motor")
with col2:
    st.metric(label="RATA2 KECEPATAN", value="45 km/jam", delta="Normal")
with col3:
    st.metric(label="KEMACETAN", value="15%", delta="Rendah")
with col4:
    st.metric(label="PELANGGARAN", value="12", delta="CCTV 01")

st.markdown("---")

# --- BARIS 2: TABEL KONDISI & GRAFIK ---
col_table, col_chart = st.columns([1, 1])

with col_table:
    st.markdown("📋 **Kondisi Arus Saat Ini**")
    # Data dummy sesuai keinginanmu
    data_kondisi = {
        'No': [1, 2, 3, 4],
        'Jenis': ['Sepeda Motor', 'Mobil Pribadi', 'Truk', 'Bis'],
        'Jumlah': [750, 400, 65, 30]
    }
    df_kondisi = pd.DataFrame(data_kondisi)
    st.table(df_kondisi.set_index('No'))

with col_chart:
    st.markdown("📊 **Statistik Volume Kendaraan**")
    fig = px.bar(df_kondisi, x='Jenis', y='Jumlah', 
                 color='Jenis',
                 color_discrete_map={'Sepeda Motor':'#3c8dbc', 'Mobil Pribadi':'#dd4b39', 'Truk':'#00a65a', 'Bis':'#f39c12'})
    fig.update_layout(showlegend=False, height=300, margin=dict(t=0, b=0, l=0, r=0))
    st.plotly_chart(fig, use_container_width=True)

# --- BARIS 3: REAL-TIME LOG ---
st.markdown("🕒 **Log Hitungan Terakhir (Kamera AI)**")
log_data = pd.DataFrame({
    'Waktu': ['10:15:01', '10:14:55', '10:14:40', '10:14:30'],
    'Objek': ['Mobil', 'Motor', 'Motor', 'Truk'],
    'Kecepatan': ['52 km/h', '40 km/h', '38 km/h', '25 km/h'],
    'Akurasi AI': ['98%', '95%', '97%', '92%']
})
st.dataframe(log_data, use_container_width=True)import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="SISMAKADIS 1.0 - Monitoring", layout="wide")

# --- CUSTOM CSS (Agar Mirip Screenshot) ---
st.markdown("""
    <style>
    /* Mengubah warna Sidebar jadi Gelap */
    [data-testid="stSidebar"] {
        background-color: #222d32;
        color: white;
    }
    /* Warna teks menu sidebar */
    [data-testid="stSidebar"] .stMarkdown p {
        color: #b8c7ce;
    }
    /* Mengatur Card Statistik */
    .stMetric {
        background-color: #ffffff;
        border-top: 3px solid #00c0ef; /* Warna biru atas card */
        padding: 15px;
        border-radius: 5px;
        box-shadow: 0 1px 1px rgba(0,0,0,0.1);
    }
    /* Styling Header Dashboard */
    .main-header {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: -10px;
    }
    .sub-header {
        color: #666;
        font-size: 14px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (NAVIGASI) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=70) # Foto profil admin
    st.markdown("**Indra Adikusuma** \n*Admin*")
    st.markdown("---")
    
    st.markdown("🔍 **Navigation**")
    menu = st.radio("", ["Dashboard", "Master Setup", "Master Kendaraan", "Rekapitulasi", "Report", "Backup Database"])
    
    st.markdown("---")
    if st.button("Collapse"):
        st.write("Sidebar Collapsed")

# --- MAIN CONTENT ---
st.markdown('<p class="main-header">Dashboard <span style="font-weight:normal; font-size:16px; color:#999;">Overview & statistic</span></p>', unsafe_allow_html=True)

# Banner Hijau Welcome
st.success("✅ **Welcome To SISMAKADIS Version 1.0**. Aplikasi Sistem Informasi Monitoring Arus Lalu Lintas Pintar.")

# --- BARIS 1: KARTU STATISTIK (4 Kolom) ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="TOTAL KENDARAAN", value="1,245", delta="Mobil & Motor")
with col2:
    st.metric(label="RATA2 KECEPATAN", value="45 km/jam", delta="Normal")
with col3:
    st.metric(label="KEMACETAN", value="15%", delta="Rendah")
with col4:
    st.metric(label="PELANGGARAN", value="12", delta="CCTV 01")

st.markdown("---")

# --- BARIS 2: TABEL KONDISI & GRAFIK ---
col_table, col_chart = st.columns([1, 1])

with col_table:
    st.markdown("📋 **Kondisi Arus Saat Ini**")
    # Data dummy sesuai keinginanmu
    data_kondisi = {
        'No': [1, 2, 3, 4],
        'Jenis': ['Sepeda Motor', 'Mobil Pribadi', 'Truk', 'Bis'],
        'Jumlah': [750, 400, 65, 30]
    }
    df_kondisi = pd.DataFrame(data_kondisi)
    st.table(df_kondisi.set_index('No'))

with col_chart:
    st.markdown("📊 **Statistik Volume Kendaraan**")
    fig = px.bar(df_kondisi, x='Jenis', y='Jumlah', 
                 color='Jenis',
                 color_discrete_map={'Sepeda Motor':'#3c8dbc', 'Mobil Pribadi':'#dd4b39', 'Truk':'#00a65a', 'Bis':'#f39c12'})
    fig.update_layout(showlegend=False, height=300, margin=dict(t=0, b=0, l=0, r=0))
    st.plotly_chart(fig, use_container_width=True)

# --- BARIS 3: REAL-TIME LOG ---
st.markdown("🕒 **Log Hitungan Terakhir (Kamera AI)**")
log_data = pd.DataFrame({
    'Waktu': ['10:15:01', '10:14:55', '10:14:40', '10:14:30'],
    'Objek': ['Mobil', 'Motor', 'Motor', 'Truk'],
    'Kecepatan': ['52 km/h', '40 km/h', '38 km/h', '25 km/h'],
    'Akurasi AI': ['98%', '95%', '97%', '92%']
})
st.dataframe(log_data, use_container_width=True)import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="SISMAKADIS 1.0 - Monitoring", layout="wide")

# --- CUSTOM CSS (Agar Mirip Screenshot) ---
st.markdown("""
    <style>
    /* Mengubah warna Sidebar jadi Gelap */
    [data-testid="stSidebar"] {
        background-color: #222d32;
        color: white;
    }
    /* Warna teks menu sidebar */
    [data-testid="stSidebar"] .stMarkdown p {
        color: #b8c7ce;
    }
    /* Mengatur Card Statistik */
    .stMetric {
        background-color: #ffffff;
        border-top: 3px solid #00c0ef; /* Warna biru atas card */
        padding: 15px;
        border-radius: 5px;
        box-shadow: 0 1px 1px rgba(0,0,0,0.1);
    }
    /* Styling Header Dashboard */
    .main-header {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: -10px;
    }
    .sub-header {
        color: #666;
        font-size: 14px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (NAVIGASI) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=70) # Foto profil admin
    st.markdown("**Indra Adikusuma** \n*Admin*")
    st.markdown("---")
    
    st.markdown("🔍 **Navigation**")
    menu = st.radio("", ["Dashboard", "Master Setup", "Master Kendaraan", "Rekapitulasi", "Report", "Backup Database"])
    
    st.markdown("---")
    if st.button("Collapse"):
        st.write("Sidebar Collapsed")

# --- MAIN CONTENT ---
st.markdown('<p class="main-header">Dashboard <span style="font-weight:normal; font-size:16px; color:#999;">Overview & statistic</span></p>', unsafe_allow_html=True)

# Banner Hijau Welcome
st.success("✅ **Welcome To SISMAKADIS Version 1.0**. Aplikasi Sistem Informasi Monitoring Arus Lalu Lintas Pintar.")

# --- BARIS 1: KARTU STATISTIK (4 Kolom) ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="TOTAL KENDARAAN", value="1,245", delta="Mobil & Motor")
with col2:
    st.metric(label="RATA2 KECEPATAN", value="45 km/jam", delta="Normal")
with col3:
    st.metric(label="KEMACETAN", value="15%", delta="Rendah")
with col4:
    st.metric(label="PELANGGARAN", value="12", delta="CCTV 01")

st.markdown("---")

# --- BARIS 2: TABEL KONDISI & GRAFIK ---
col_table, col_chart = st.columns([1, 1])

with col_table:
    st.markdown("📋 **Kondisi Arus Saat Ini**")
    # Data dummy sesuai keinginanmu
    data_kondisi = {
        'No': [1, 2, 3, 4],
        'Jenis': ['Sepeda Motor', 'Mobil Pribadi', 'Truk', 'Bis'],
        'Jumlah': [750, 400, 65, 30]
    }
    df_kondisi = pd.DataFrame(data_kondisi)
    st.table(df_kondisi.set_index('No'))

with col_chart:
    st.markdown("📊 **Statistik Volume Kendaraan**")
    fig = px.bar(df_kondisi, x='Jenis', y='Jumlah', 
                 color='Jenis',
                 color_discrete_map={'Sepeda Motor':'#3c8dbc', 'Mobil Pribadi':'#dd4b39', 'Truk':'#00a65a', 'Bis':'#f39c12'})
    fig.update_layout(showlegend=False, height=300, margin=dict(t=0, b=0, l=0, r=0))
    st.plotly_chart(fig, use_container_width=True)

# --- BARIS 3: REAL-TIME LOG ---
st.markdown("🕒 **Log Hitungan Terakhir (Kamera AI)**")
log_data = pd.DataFrame({
    'Waktu': ['10:15:01', '10:14:55', '10:14:40', '10:14:30'],
    'Objek': ['Mobil', 'Motor', 'Motor', 'Truk'],
    'Kecepatan': ['52 km/h', '40 km/h', '38 km/h', '25 km/h'],
    'Akurasi AI': ['98%', '95%', '97%', '92%']
})
st.dataframe(log_data, use_container_width=True)import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="SISMAKADIS 1.0 - Monitoring", layout="wide")

# --- CUSTOM CSS (Agar Mirip Screenshot) ---
st.markdown("""
    <style>
    /* Mengubah warna Sidebar jadi Gelap */
    [data-testid="stSidebar"] {
        background-color: #222d32;
        color: white;
    }
    /* Warna teks menu sidebar */
    [data-testid="stSidebar"] .stMarkdown p {
        color: #b8c7ce;
    }
    /* Mengatur Card Statistik */
    .stMetric {
        background-color: #ffffff;
        border-top: 3px solid #00c0ef; /* Warna biru atas card */
        padding: 15px;
        border-radius: 5px;
        box-shadow: 0 1px 1px rgba(0,0,0,0.1);
    }
    /* Styling Header Dashboard */
    .main-header {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: -10px;
    }
    .sub-header {
        color: #666;
        font-size: 14px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (NAVIGASI) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=70) # Foto profil admin
    st.markdown("**Indra Adikusuma** \n*Admin*")
    st.markdown("---")
    
    st.markdown("🔍 **Navigation**")
    menu = st.radio("", ["Dashboard", "Master Setup", "Master Kendaraan", "Rekapitulasi", "Report", "Backup Database"])
    
    st.markdown("---")
    if st.button("Collapse"):
        st.write("Sidebar Collapsed")

# --- MAIN CONTENT ---
st.markdown('<p class="main-header">Dashboard <span style="font-weight:normal; font-size:16px; color:#999;">Overview & statistic</span></p>', unsafe_allow_html=True)

# Banner Hijau Welcome
st.success("✅ **Welcome To SISMAKADIS Version 1.0**. Aplikasi Sistem Informasi Monitoring Arus Lalu Lintas Pintar.")

# --- BARIS 1: KARTU STATISTIK (4 Kolom) ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="TOTAL KENDARAAN", value="1,245", delta="Mobil & Motor")
with col2:
    st.metric(label="RATA2 KECEPATAN", value="45 km/jam", delta="Normal")
with col3:
    st.metric(label="KEMACETAN", value="15%", delta="Rendah")
with col4:
    st.metric(label="PELANGGARAN", value="12", delta="CCTV 01")

st.markdown("---")

# --- BARIS 2: TABEL KONDISI & GRAFIK ---
col_table, col_chart = st.columns([1, 1])

with col_table:
    st.markdown("📋 **Kondisi Arus Saat Ini**")
    # Data dummy sesuai keinginanmu
    data_kondisi = {
        'No': [1, 2, 3, 4],
        'Jenis': ['Sepeda Motor', 'Mobil Pribadi', 'Truk', 'Bis'],
        'Jumlah': [750, 400, 65, 30]
    }
    df_kondisi = pd.DataFrame(data_kondisi)
    st.table(df_kondisi.set_index('No'))

with col_chart:
    st.markdown("📊 **Statistik Volume Kendaraan**")
    fig = px.bar(df_kondisi, x='Jenis', y='Jumlah', 
                 color='Jenis',
                 color_discrete_map={'Sepeda Motor':'#3c8dbc', 'Mobil Pribadi':'#dd4b39', 'Truk':'#00a65a', 'Bis':'#f39c12'})
    fig.update_layout(showlegend=False, height=300, margin=dict(t=0, b=0, l=0, r=0))
    st.plotly_chart(fig, use_container_width=True)

# --- BARIS 3: REAL-TIME LOG ---
st.markdown("🕒 **Log Hitungan Terakhir (Kamera AI)**")
log_data = pd.DataFrame({
    'Waktu': ['10:15:01', '10:14:55', '10:14:40', '10:14:30'],
    'Objek': ['Mobil', 'Motor', 'Motor', 'Truk'],
    'Kecepatan': ['52 km/h', '40 km/h', '38 km/h', '25 km/h'],
    'Akurasi AI': ['98%', '95%', '97%', '92%']
})
st.dataframe(log_data, use_container_width=True)import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="SISMAKADIS 1.0 - Monitoring", layout="wide")

# --- CUSTOM CSS (Agar Mirip Screenshot) ---
st.markdown("""
    <style>
    /* Mengubah warna Sidebar jadi Gelap */
    [data-testid="stSidebar"] {
        background-color: #222d32;
        color: white;
    }
    /* Warna teks menu sidebar */
    [data-testid="stSidebar"] .stMarkdown p {
        color: #b8c7ce;
    }
    /* Mengatur Card Statistik */
    .stMetric {
        background-color: #ffffff;
        border-top: 3px solid #00c0ef; /* Warna biru atas card */
        padding: 15px;
        border-radius: 5px;
        box-shadow: 0 1px 1px rgba(0,0,0,0.1);
    }
    /* Styling Header Dashboard */
    .main-header {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: -10px;
    }
    .sub-header {
        color: #666;
        font-size: 14px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (NAVIGASI) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=70) # Foto profil admin
    st.markdown("**Indra Adikusuma** \n*Admin*")
    st.markdown("---")
    
    st.markdown("🔍 **Navigation**")
    menu = st.radio("", ["Dashboard", "Master Setup", "Master Kendaraan", "Rekapitulasi", "Report", "Backup Database"])
    
    st.markdown("---")
    if st.button("Collapse"):
        st.write("Sidebar Collapsed")

# --- MAIN CONTENT ---
st.markdown('<p class="main-header">Dashboard <span style="font-weight:normal; font-size:16px; color:#999;">Overview & statistic</span></p>', unsafe_allow_html=True)

# Banner Hijau Welcome
st.success("✅ **Welcome To SISMAKADIS Version 1.0**. Aplikasi Sistem Informasi Monitoring Arus Lalu Lintas Pintar.")

# --- BARIS 1: KARTU STATISTIK (4 Kolom) ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="TOTAL KENDARAAN", value="1,245", delta="Mobil & Motor")
with col2:
    st.metric(label="RATA2 KECEPATAN", value="45 km/jam", delta="Normal")
with col3:
    st.metric(label="KEMACETAN", value="15%", delta="Rendah")
with col4:
    st.metric(label="PELANGGARAN", value="12", delta="CCTV 01")

st.markdown("---")

# --- BARIS 2: TABEL KONDISI & GRAFIK ---
col_table, col_chart = st.columns([1, 1])

with col_table:
    st.markdown("📋 **Kondisi Arus Saat Ini**")
    # Data dummy sesuai keinginanmu
    data_kondisi = {
        'No': [1, 2, 3, 4],
        'Jenis': ['Sepeda Motor', 'Mobil Pribadi', 'Truk', 'Bis'],
        'Jumlah': [750, 400, 65, 30]
    }
    df_kondisi = pd.DataFrame(data_kondisi)
    st.table(df_kondisi.set_index('No'))

with col_chart:
    st.markdown("📊 **Statistik Volume Kendaraan**")
    fig = px.bar(df_kondisi, x='Jenis', y='Jumlah', 
                 color='Jenis',
                 color_discrete_map={'Sepeda Motor':'#3c8dbc', 'Mobil Pribadi':'#dd4b39', 'Truk':'#00a65a', 'Bis':'#f39c12'})
    fig.update_layout(showlegend=False, height=300, margin=dict(t=0, b=0, l=0, r=0))
    st.plotly_chart(fig, use_container_width=True)

# --- BARIS 3: REAL-TIME LOG ---
st.markdown("🕒 **Log Hitungan Terakhir (Kamera AI)**")
log_data = pd.DataFrame({
    'Waktu': ['10:15:01', '10:14:55', '10:14:40', '10:14:30'],
    'Objek': ['Mobil', 'Motor', 'Motor', 'Truk'],
    'Kecepatan': ['52 km/h', '40 km/h', '38 km/h', '25 km/h'],
    'Akurasi AI': ['98%', '95%', '97%', '92%']
})
st.dataframe(log_data, use_container_width=True)import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="SISMAKADIS 1.0 - Monitoring", layout="wide")

# --- CUSTOM CSS (Agar Mirip Screenshot) ---
st.markdown("""
    <style>
    /* Mengubah warna Sidebar jadi Gelap */
    [data-testid="stSidebar"] {
        background-color: #222d32;
        color: white;
    }
    /* Warna teks menu sidebar */
    [data-testid="stSidebar"] .stMarkdown p {
        color: #b8c7ce;
    }
    /* Mengatur Card Statistik */
    .stMetric {
        background-color: #ffffff;
        border-top: 3px solid #00c0ef; /* Warna biru atas card */
        padding: 15px;
        border-radius: 5px;
        box-shadow: 0 1px 1px rgba(0,0,0,0.1);
    }
    /* Styling Header Dashboard */
    .main-header {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: -10px;
    }
    .sub-header {
        color: #666;
        font-size: 14px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (NAVIGASI) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=70) # Foto profil admin
    st.markdown("**Indra Adikusuma** \n*Admin*")
    st.markdown("---")
    
    st.markdown("🔍 **Navigation**")
    menu = st.radio("", ["Dashboard", "Master Setup", "Master Kendaraan", "Rekapitulasi", "Report", "Backup Database"])
    
    st.markdown("---")
    if st.button("Collapse"):
        st.write("Sidebar Collapsed")

# --- MAIN CONTENT ---
st.markdown('<p class="main-header">Dashboard <span style="font-weight:normal; font-size:16px; color:#999;">Overview & statistic</span></p>', unsafe_allow_html=True)

# Banner Hijau Welcome
st.success("✅ **Welcome To SISMAKADIS Version 1.0**. Aplikasi Sistem Informasi Monitoring Arus Lalu Lintas Pintar.")

# --- BARIS 1: KARTU STATISTIK (4 Kolom) ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="TOTAL KENDARAAN", value="1,245", delta="Mobil & Motor")
with col2:
    st.metric(label="RATA2 KECEPATAN", value="45 km/jam", delta="Normal")
with col3:
    st.metric(label="KEMACETAN", value="15%", delta="Rendah")
with col4:
    st.metric(label="PELANGGARAN", value="12", delta="CCTV 01")

st.markdown("---")

# --- BARIS 2: TABEL KONDISI & GRAFIK ---
col_table, col_chart = st.columns([1, 1])

with col_table:
    st.markdown("📋 **Kondisi Arus Saat Ini**")
    # Data dummy sesuai keinginanmu
    data_kondisi = {
        'No': [1, 2, 3, 4],
        'Jenis': ['Sepeda Motor', 'Mobil Pribadi', 'Truk', 'Bis'],
        'Jumlah': [750, 400, 65, 30]
    }
    df_kondisi = pd.DataFrame(data_kondisi)
    st.table(df_kondisi.set_index('No'))

with col_chart:
    st.markdown("📊 **Statistik Volume Kendaraan**")
    fig = px.bar(df_kondisi, x='Jenis', y='Jumlah', 
                 color='Jenis',
                 color_discrete_map={'Sepeda Motor':'#3c8dbc', 'Mobil Pribadi':'#dd4b39', 'Truk':'#00a65a', 'Bis':'#f39c12'})
    fig.update_layout(showlegend=False, height=300, margin=dict(t=0, b=0, l=0, r=0))
    st.plotly_chart(fig, use_container_width=True)

# --- BARIS 3: REAL-TIME LOG ---
st.markdown("🕒 **Log Hitungan Terakhir (Kamera AI)**")
log_data = pd.DataFrame({
    'Waktu': ['10:15:01', '10:14:55', '10:14:40', '10:14:30'],
    'Objek': ['Mobil', 'Motor', 'Motor', 'Truk'],
    'Kecepatan': ['52 km/h', '40 km/h', '38 km/h', '25 km/h'],
    'Akurasi AI': ['98%', '95%', '97%', '92%']
})
st.dataframe(log_data, use_container_width=True)
