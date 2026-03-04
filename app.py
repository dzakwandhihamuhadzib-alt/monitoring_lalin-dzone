from ultralytics import YOLO
import cv2
import csv
import datetime
import os

# 1. SETTING DASAR
nama_video = "video-tes_hitungkendaraan.MP4" 
nama_file_csv = "laporan_deteksi_kendaraan.csv"
model = YOLO("yolov8n.pt") 

cap = cv2.VideoCapture(nama_video)
track_history = {} 

# Membuat Header Baru (Hapus dulu file lama agar tidak double header)
if not os.path.exists(nama_file_csv):
    with open(nama_file_csv, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Jam', 'Jenis Kendaraan', 'Kecepatan'])

print("--- PROGRAM DIMULAI (TEKAN 'Q' UNTUK BERHENTI) ---")

while True:
    success, img = cap.read()
    if not success: break

    # Menggunakan model.track agar ID kendaraan konsisten (penting untuk hitung kecepatan)
    results = model.track(img, persist=True, classes=[2, 3, 5, 7], verbose=False)

    # Cek apakah ada objek yang terdeteksi
    if results[0].boxes.id is not None:
        boxes = results[0].boxes.xyxy.cpu().numpy().astype(int)
        ids = results[0].boxes.id.cpu().numpy().astype(int)
        clss = results[0].boxes.cls.cpu().numpy().astype(int)

        for box, track_id, cls in zip(boxes, ids, clss):
            x1, y1, x2, y2 = box
            label = model.names[cls]
            pusat_y = (y1 + y2) // 2 

            # HITUNG KECEPATAN
            kmh = 0
            if track_id in track_history:
                selisih = abs(pusat_y - track_history[track_id])
                kmh = int(selisih * 5.0) # Sesuaikan angka 5.0 ini jika terlalu lambat/cepat
            
            track_history[track_id] = pusat_y
            waktu_skrg = datetime.datetime.now().strftime("%H:%M:%S")

            # --- BAGIAN KRUSIAL: SIMPAN DATA ---
            # Pastikan blok ini sejajar di bawah 'for box...', bukan di dalam 'if kmh > 0'
            try:
                with open(nama_file_csv, mode='a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([waktu_skrg, label, f"{kmh} km/jam"])
            except PermissionError:
                # Jika file dibuka di Excel, tampilkan peringatan di layar saja
                cv2.putText(img, "CLOSE EXCEL!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

            # VISUALISASI DI LAYAR
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(img, f"ID:{track_id} {label} {kmh} km/h", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("Monitoring Kecepatan", img)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()
print(f"Selesai! Cek file di: {os.path.abspath(nama_file_csv)}")
