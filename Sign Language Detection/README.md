# Be-Heard

# Sign Language Detection

## Overview

The **Sign Language Detection** folder in the **Be Heard** project focuses on converting sign language gestures into English text. It contains all the code and model modules necessary for this task. This module utilizes advanced machine learning algorithms and computer vision techniques to recognize and translate sign language in real-time.

## Use Case

### Sign Language to English Text Conversion
- **Problem**: Sign language users often struggle to communicate with non-sign language speakers in various environments, such as classrooms or public spaces.
- **Solution**: This module accurately captures the gestures of sign language and converts them into English text, facilitating smooth, real-time communication between sign language users and those who do not know sign language.

## Project Structure

This folder contains the following key components:

- **BH-V1.py**: The main script that implements the sign language recognition algorithm, processes video input, and outputs the recognized gestures as text.
- **requirements.txt**: A file listing the necessary Python packages required to run the module.
- **my_model.keras**: Model generated from version_1

## Installation Instructions

To set up the Sign Language Detection module, follow these steps:

### By Cloning the Repo and Executing

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Sugabiyrarosha1/be-heard.git
   ```

2. **Go to the Sign Language Detection folder**:
   Navigate to the `Sign Language Detection` folder.

3. **Install required packages**:
   Make sure you have Python 3.x installed. Then, run:
   ```bash
   pip install -r requirements.txt
   ```

4. **Go to the BH-V1.py file**:
   Navigate to the BH-V1.ipynb file.

5. **Go to the Main Section and Run the main code**:
   Scroll to the last section of the file where the main function is implemented.
   - This will use the model `my_model.keras` located in `Be-Heard/Sign Language Detection/Code`.

### Input Requirements:

Ensure your camera is connected and accessible to the script.
The module will process the sign language gestures captured through the camera in real-time.

### Expected Output:

The recognized gestures will be displayed as English text on the screen.
