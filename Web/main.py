from flask import Flask, render_template, request, Response
import cv2
import numpy as np

app = Flask(__name__)
camera = cv2.VideoCapture(0)  # Sử dụng camera mặc định (0)
selected_filter = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/apply_filter', methods=['POST'])
def apply_filter():
    global selected_filter
    selected_filter = request.form['filter']
    return '', 204

def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        if selected_filter:
            frame = apply_color_filter(frame, selected_filter)
        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            break
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def apply_color_filter(frame, filter_name):
    if filter_name == 'negative':
        return cv2.bitwise_not(frame)
    elif filter_name == 'gray':
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return frame

if __name__ == '__main__':
    app.run(debug=True)
