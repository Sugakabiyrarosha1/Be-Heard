from flask import Flask, render_template, Response, request, jsonify
import cv2
import numpy as np
import mediapipe as mp
from tensorflow.keras.models import load_model
from collections import deque
from googletrans import Translator
from gtts import gTTS
from io import BytesIO

app = Flask(__name__)

# Initialize Mediapipe holistic and drawing utilities
mp_holistic = mp.solutions.holistic
mp_drawing = mp.solutions.drawing_utils

# Initialize translator
translator = Translator()

# Load pre-trained model
model = load_model('model/action_V2_20.keras')

# Actions that the model predicts
actions = np.array(['Hello', 'ILoveYou', 'No', 'Yes', 'ThankYou', 'Please', 'Sorry', 'A', 'E', 'F', 'H', 'I', 'M', 'N', 'O', 'R', 'S', 'T', 'My', 'Name'])

# Initialize buffer for storing keypoints for multiple frames (sequence)
sequence = deque(maxlen=30)

# Variables to store detected action and translated text
detected_action = ""
translated_text = ""

# Define functions for Mediapipe detection and drawing
def mediapipe_detection(image, model):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    results = model.process(image)
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    return image, results

def draw_styled_landmarks(image, results):
    # Draw face landmarks without the grid lines (customized drawing)
    if results.face_landmarks:
        mp_drawing.draw_landmarks(
            image,
            results.face_landmarks,
            connections=None,  # No grid connections for the face
            landmark_drawing_spec=None  # No landmarks drawn on the face
        )

    # Draw pose connections
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(
            image,
            results.pose_landmarks,
            mp_holistic.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2)  # Pose points
        )

    # Draw left-hand connections
    if results.left_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,
            results.left_hand_landmarks,
            mp_holistic.HAND_CONNECTIONS,
            landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 255), thickness=2, circle_radius=2)  # Left hand
        )

    # Draw right-hand connections
    if results.right_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,
            results.right_hand_landmarks,
            mp_holistic.HAND_CONNECTIONS,
            landmark_drawing_spec=mp_drawing.DrawingSpec(color=(255, 0, 255), thickness=2, circle_radius=2)  # Right hand
        )

def extract_keypoints(results):
    pose = np.array([[res.x, res.y, res.z, res.visibility] for res in results.pose_landmarks.landmark]).flatten() if results.pose_landmarks else np.zeros(33*4)
    face = np.array([[res.x, res.y, res.z] for res in results.face_landmarks.landmark]).flatten() if results.face_landmarks else np.zeros(468*3)
    lh = np.array([[res.x, res.y, res.z] for res in results.left_hand_landmarks.landmark]).flatten() if results.left_hand_landmarks else np.zeros(21*3)
    rh = np.array([[res.x, res.y, res.z] for res in results.right_hand_landmarks.landmark]).flatten() if results.right_hand_landmarks else np.zeros(21*3)
    return np.concatenate([pose, face, lh, rh])

# Video feed generator function
def gen_frames():
    global detected_action
    cap = cv2.VideoCapture(0)
    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        while True:
            success, frame = cap.read()
            if not success:
                break
            
            # Make detection and extract landmarks
            image, results = mediapipe_detection(frame, holistic)
            draw_styled_landmarks(image, results)
            keypoints = extract_keypoints(results)
            sequence.append(keypoints)

            # Only make predictions if we have enough frames (e.g., 30 frames)
            if len(sequence) == 30:
                input_sequence = np.array(sequence).reshape(1, 30, -1)
                prediction = model.predict(input_sequence)
                detected_action = actions[np.argmax(prediction)]

            # Display detected action
            cv2.putText(image, detected_action, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

            # Encode the frame as JPEG
            ret, buffer = cv2.imencode('.jpg', image)
            frame = buffer.tobytes()

            # Yield the frame in byte format
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/translate', methods=['POST'])
def translate():
    global detected_action, translated_text
    target_language = request.form['language']
    
    # Default message if no action detected
    if not detected_action:
        detected_action = "No action detected"
    
    # If target language is English, skip translation
    if target_language == 'en':
        translated_text = detected_action
    else:
        translated_text = translator.translate(detected_action, dest=target_language).text

    return jsonify({'translated_text': translated_text})

@app.route('/play_audio', methods=['POST'])
def play_audio():
    global translated_text
    target_language = request.form['language']

    # Translate if text is not yet translated to target language
    if not translated_text or target_language != 'en':
        translated_text = translate_text(detected_action, target_language)

    if translated_text:
        tts = gTTS(translated_text, lang=target_language)
        audio_buffer = BytesIO()
        tts.write_to_fp(audio_buffer)
        audio_buffer.seek(0)
        return Response(audio_buffer, mimetype="audio/mpeg")
    return jsonify({'error': 'No text to play'}), 400

def translate_text(text, target_language):
    return text if target_language == 'en' else translator.translate(text, dest=target_language).text

if __name__ == '__main__':
    app.run(debug=True)
