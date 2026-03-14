import streamlit as st
import cv2
from ultralytics import YOLO
import yt_dlp

# Gunakan model yang paling kecil (Nano) agar tidak error limit memori di Streamlit
@st.cache_resource
def load_model():
    return YOLO("yolov8n.pt")

model = load_model()

# Fungsi untuk ambil stream YouTube
def get_url(url):
    ydl_opts = {'format': 'best', 'quiet': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        return ydl.extract_info(url, download=False)['url']

# Di bagian menu "PILIH KAMERA"
if st.button("MULAI MONITORING"):
    st.write("Menghubungkan ke Server CCTV...")
    try:
        stream_url = get_url(cctv_list[selected_cctv])
        cap = cv2.VideoCapture(stream_url)
        st_frame = st.empty() # Tempat frame video

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            # AI Detection (Opsional: jalankan setiap 5 frame agar tidak berat)
            results = model(frame, stream=True, classes=[2, 3, 5, 7])
            
            for r in results:
                frame = r.plot() # Gambar kotak deteksi

            # Tampilkan ke Streamlit
            st_frame.image(frame, channels="BGR", use_container_width=True)
            
    except Exception as e:
        st.error(f"Gagal memuat video: {e}")
