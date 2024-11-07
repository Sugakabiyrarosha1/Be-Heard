from flask import Flask, render_template, Response, jsonify, request
import cv2
import numpy as np
import mediapipe as mp
from tensorflow.keras.models import load_model
from collections import deque
from googletrans import Translator
from gtts import gTTS
import os

app = Flask(__name__)

# Load the trained model and define the actions
model = load_model('action_V2_20.keras')
actions = np.array(['Hello', 'ILoveYou', 'No', 'Yes', 'ThankYou', 'Please', 'Sorry', 'A', 'E', 'F', 'H', 'I', 'M', 'N', 'O', 'R', 'S', 'T', 'My', 'Name'])
sequence = deque(maxlen=30)
translator = Translator()

# Initialize Mediapipe holistic model
mp_holistic = mp.solutions.holistic

# Video feed function with real-time prediction overlay
def generate_frames():
    camera = cv2.VideoCapture(0)
    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        while True:
            success, frame = camera.read()
            if not success:
                break

            # Process and predict
            image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = holistic.process(image_rgb)
            if results.pose_landmarks:
                # Extract landmarks and prepare for prediction
                landmarks = [landmark.x for landmark in results.pose_landmarks.landmark] + \
                            [landmark.y for landmark in results.pose_landmarks.landmark] + \
                            [landmark.z for landmark in results.pose_landmarks.landmark]
                sequence.append(np.array(landmarks))
                if len(sequence) == 30:
                    res = model.predict(np.expand_dims(sequence, axis=0))[0]
                    action = actions[np.argmax(res)]
                    confidence = res[np.argmax(res)]
                    cv2.putText(frame, f'{action} ({confidence:.2%})', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

            # Encode frame to JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    text = data['text']
    language = data['language']
    translated_text = translator.translate(text, dest=language).text
    return jsonify({'translated_text': translated_text})

@app.route('/text_to_speech', methods=['POST'])
def text_to_speech():
    data = request.get_json()
    text = data['text']
    language = data['language']
    speed = data['speed']
    tts = gTTS(text=text, lang=language, slow=(speed < 1))
    audio_path = 'static/output.mp3'
    tts.save(audio_path)
    return jsonify({'audio_url': f'/{audio_path}'})

if __name__ == '__main__':
    app.run(debug=True)
