# Be Heard: AI-Driven Sign Language Translation System

## Project Overview
**Be Heard** is an AI-powered system that bridges the communication gap for users who rely on sign language by converting visual gestures into text and audio. It allows seamless interaction between sign language users and non-sign language speakers, offering multi-language support for global accessibility.

We are mainly focusing on using American Sign Language (ASL) for this project.

This project implements advanced machine learning models and AI technologies to:
- Convert Sign Language to English text.
- Translate English text into any chosen language.
- Convert the translated text into audio.

## Use Cases

### 1. Sign Language to English Text Conversion
- **Problem**: Sign language users often struggle to communicate with non-sign language speakers.
- **Solution**: This feature converts sign language gestures into English text, enabling smoother communication in real-time.

### 2. English Text Translation into Any Other Language
- **Problem**: Multilingual communication is challenging when speakers don’t share a common language.
- **Solution**: Once the sign language is converted into English text, this feature translates the text into other languages such as French, Spanish, or Mandarin using high-precision translation algorithms.

### 3. Text to Audio Conversion
- **Problem**: In some contexts, text-based communication is not ideal, especially for the visually impaired or in social scenarios that prefer verbal interaction.
- **Solution**: This feature converts the translated text into speech, allowing the system to communicate via audio output for enhanced accessibility.


## Project Structure

Be-Heard/
├── app.py            # Main application file
├── requirements.txt  # Python dependencies
├── README.md         # Project documentation
├── templates/        # HTML templates for the web interface
├── logs/             # Logs for monitoring application performance

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
Install required packages: Make sure you have Python 3.x installed. Then, run:

pip install -r requirements.txt
Download necessary data files: Ensure that all data files (such as processed images) are available in the appropriate directories.

Input Requirements: Ensure your camera is connected and accessible. The module will process sign language gestures captured in real-time.
Expected Output: The recognized gestures will be displayed as English text on the screen.

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


 Team
 
-Sugakabiyrarosha
-Fatimah Al Musawi
-Nivetha Rajamani

