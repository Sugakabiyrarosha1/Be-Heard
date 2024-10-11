# Be-Heard

# Sign Language Detection

## Overview

The **Sign Language Detection** branch is a key component of the **Be Heard** project, focusing specifically on converting sign language gestures into English text. This module utilizes advanced machine learning algorithms and computer vision techniques to recognize and translate sign language in real-time.

## Data

- **Processed_Alpha_Images**: Contains the processed images in NPY format of the alphabets and numbers.
- **Words**: Contains the processed images in NPY format of various words.

## Use Case

### Sign Language to English Text Conversion
- **Problem**: Sign language users often struggle to communicate with non-sign language speakers in various environments, such as classrooms or public spaces.
- **Solution**: This module accurately captures the gestures of sign language and converts them into English text, facilitating smooth, real-time communication between sign language users and those who do not know sign language.

## Project Structure

This folder contains the following key components:

- **BH-V1.py**: The main script that implements the sign language recognition algorithm, processes video input, and outputs the recognized gestures as text.
- **Processed_Alpha_Images/**: Directory containing processed images of the alphabets and numbers in NPY format.
- **Words/**: Directory containing processed images of various words in NPY format.
- **requirements.txt**: A file listing the necessary Python packages required to run the module.

## Installation Instructions

To set up the Sign Language Detection module, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Sugabiyrarosha1/be-heard.git

2. **Install required packages: Make sure you have Python 3.x installed. Then, run:**:
   ```bash
   pip install -r requirements.txt
  
3. Download the necessary data files: Ensure that the Processed_Alpha_Images and Words NPY files are available in the appropriate directories.

Usage Examples
To run the sign language detection module, use the following command:
  python BH-V1.py

### Input Requirements:

Ensure your camera is connected and accessible to the script.
The module will process the sign language gestures captured through the camera in real-time.

### Expected Output:

The recognized gestures will be displayed as English text on the screen.

