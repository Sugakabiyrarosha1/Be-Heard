# Be Heard: AI-Driven Sign Language Translation System

## Project Overview
**Be Heard** is an innovative AI-powered application designed to bridge communication gaps by converting sign language gestures into text and audio. The system supports multilingual translation to enhance accessibility for users globally. It focuses on real-time recognition of American Sign Language (ASL) gestures, with an intuitive interface and comprehensive functionality.

### Key Features:
- **Real-time Sign Language to English Text Conversion**
- **English Text Translation into Multiple Languages**
- **Text-to-Audio Conversion**
- **User-Friendly Web Interface**

## Use Cases

### 1. Sign Language to English Text Conversion
- **Problem**: Sign language users face communication barriers with non-sign language speakers.
- **Solution**: Converts ASL gestures into English text for real-time communication.

### 2. English Text Translation
- **Problem**: Multilingual communication barriers among users.
- **Solution**: Translates English text into various languages such as French, Spanish, and Chinese, using Google Translate API.

### 3. Text-to-Audio Conversion
- **Problem**: Text-based communication may not suffice in some scenarios, e.g., for visually impaired users.
- **Solution**: Converts translated text into speech using Google Text-to-Speech (gTTS) for enhanced accessibility.

## Project Structure
```plaintext
Be-Heard/
├── app.py            # Main application backend (Flask)
├── requirements.txt  # Python dependencies
├── README.md         # Project documentation
├── templates/        # HTML templates for the web interface
├── logs/             # Logs for monitoring performance and actions
├── model/            # Pre-trained model action_V2_20.keras for Sign Language detection
```


### Features

Real-time sign language detection using machine learning models.

User-friendly web interface for ease of access.

Logging system for monitoring and debugging.

Easy setup and deployment with requirements.txt.


## Setup Instructions

To set up the Be Heard project, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Sugakabiyrarosha1/be-heard.git
   cd be-heard

2. Install required packages: Make sure you have Python 3.x installed. Then, run:

3. Download Required Files : 
Ensure all necessary files, including the pre-trained model (action_V2_20.keras), are present in the model/ directory.

4. pip install -r requirements.txt
Download necessary data files: Ensure that all data files (such as processed images) are available in the appropriate directories.

Input Requirements: Ensure your camera is connected and accessible. The module will process sign language gestures captured in real-time.
Expected Output: The recognized gestures will be displayed as English text on the screen.

# Machine Learning Approach for Building the Sign Language Model

The **Be Heard** project leverages machine learning (ML) to create a real-time system capable of converting sign language gestures into text. Below is an overview of how machine learning is utilized to build the sign language recognition model:

## 1. Data Collection and Preprocessing
- **Input**: The system takes images or video frames captured by a camera, in which sign language gestures are displayed.
  
- **Preprocessing**:
  - **Mediapipe** is used to detect and extract key hand landmarks from each frame of the video. These landmarks represent the position of various points on the hand, which are essential for gesture recognition.
  - The video frames are converted into images, and relevant features (such as hand position, orientation, and movement) are extracted for model training.

## 2. Feature Engineering
- **Hand Landmarks**:  
  The Mediapipe framework detects key points on the hand (such as wrist, thumb, and finger joints). These keypoints are treated as features and serve as the input to the machine learning model.
  
- **Normalization**:  
  The extracted keypoint data is normalized to account for variations in hand size, camera distance, and orientation, ensuring consistent input for the model.

## 3. Model Selection
- **Convolutional Neural Networks (CNNs)**:  
  CNNs are often employed in computer vision tasks due to their ability to learn spatial hierarchies in data. In this project, a CNN or a hybrid model is likely used to classify the gestures based on the extracted keypoints.

- **Pretrained Models**:  
  TensorFlow and Keras frameworks are used to fine-tune pretrained models. For example, the model `action_V2_20.keras` is a trained model for sign language recognition, which can be used as-is or fine-tuned for better performance.

## 4. Model Training
- **Training Data**:  
  The model is trained on labeled datasets of sign language gestures. Each image or frame in the dataset corresponds to a specific gesture, such as a letter or a word in American Sign Language (ASL).

- **Training Process**:  
  Using TensorFlow/Keras, the model is trained with supervised learning techniques, where the features (extracted hand landmarks) are mapped to their respective labels (sign language gestures).  
  The dataset is split into training, validation, and test sets to evaluate the model’s performance.

## 5. Model Evaluation
- **Metrics**:  
  The model’s accuracy and performance are evaluated using metrics like precision, recall, and F1-score. The model’s ability to generalize to unseen data is tested by using the test set.

- **Cross-Validation**:  
  Cross-validation techniques, such as k-fold cross-validation, are used to ensure that the model performs well across different subsets of the data.

## 6. Real-Time Gesture Recognition
- **Inference**:  
  Once the model is trained and evaluated, it is deployed for real-time use. The camera captures live video, and OpenCV is used to extract frames and preprocess them.  
  The extracted hand landmarks are then passed to the trained model, which classifies the gesture and outputs the corresponding text.  
  The model provides real-time feedback, allowing users to see their gestures translated into English text.

## 7. Improvement with Multi-Language Translation
- **Text Translation**:  
  After recognizing the gesture and converting it to text, the system can then translate the text into multiple languages (e.g., French, Spanish) using the Google Translate API.

- **Text-to-Speech**:  
  The translated text is then converted to speech using the **gTTS (Google Text-to-Speech)** library, enabling spoken communication for users who may prefer audio output.

### 1. Sign Language Detection

Input: Real-time camera feed of ASL gestures.
Output: Detected gesture displayed as English tex

### 2. Translating English Text
  
Input: Provide the English text to be translated.
Expected Output: The translated text in the selected language.

### 3. Converting Text to Audio

Input: Provide the text you want to convert into speech.
Expected Output: The audio will play the translated text aloud.

For example:

### Output Examples

- **Sign Language Detection Output**:
  - Input: [Sign Language Gesture]
  - Output: "Hello, how are you?"

- **Translation Output**:
  - Input: "Hello, how are you?"
  - Output: "Bonjour, comment ça va?" (if translating to French)

- **Audio Output**:
  - Input: "Bonjour, comment ça va?"
  - Output: [Audio plays the translated text]

 
### Demo

https://github.com/user-attachments/assets/a283189d-124f-427b-9eba-9ac21df4cf04

 Be Heard Team
 
-Sugakabiyrarosha
-Fatimah Al Musawi
-Nivetha Rajamani

