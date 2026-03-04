from flask import Flask, render_template, Response
import cv2
from ultralytics import YOLO
import datetime

app = Flask(__name__)

# Load Model
model = YOLO("yolov8n.pt")
video_path = "video-tes_hitungkendaraan.MP4"

def generate_frames():
    cap = cv2.VideoCapture(video_path)
    track_history = {}

    while True:
        success, frame = cap.read()
        if not success:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0) # Ulang video jika habis
            continue
        
        # Deteksi & Tracking
        results = model.track(frame, persist=True, classes=[2, 3, 5, 7], verbose=False)
        
        if results[0].boxes.id is not None:
            boxes = results[0].boxes.xyxy.cpu().numpy().astype(int)
            ids = results[0].boxes.id.cpu().numpy().astype(int)
            clss = results[0].boxes.cls.cpu().numpy().astype(int)

            for box, track_id, cls in zip(boxes, ids, clss):
                x1, y1, x2, y2 = box
                label = model.names[cls]
                
                # Hitung Kecepatan Sederhana (Y-axis)
                pusat_y = (y1 + y2) // 2
                kmh = 0
                if track_id in track_history:
                    kmh = int(abs(pusat_y - track_history[track_id]) * 5)
                track_history[track_id] = pusat_y

                # Gambar di Frame
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, f"{label} ID:{track_id} {kmh} km/h", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Encode frame ke JPEG agar bisa dikirim ke Web
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    # Menampilkan halaman utama
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    # Jalur khusus untuk streaming video
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
