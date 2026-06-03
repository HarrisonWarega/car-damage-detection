# Automotive Damage Analysis System

An interactive machine learning application designed to identify and categorize physical structural damage on vehicles.
Users can instantly upload or drag-and-drop localized car photographs to obtain an automated structural assessment.

## Spatial Constraints & Framing

The underlying computer vision network is optimized explicitly for **three-quarter perspective shots** (capturing angled profiles of either the vehicle's front end or rear end).
For optimal prediction accuracy, ensure your uploaded imagery aligns with these perspective angles.

![Application Interface Workspace](app_screenshot.jpg)

## Neural Network Configurations

* **Core Architecture:** ResNet50 (leveraging pre-trained ImageNet deep feature extractors via Transfer Learning).
* **Dataset Volume:** Trained and validated across a dataset of approximately 1,700 localized vehicle images.
* **Target Categories:** Maps visual defects into 6 distinct classification outputs:
  * Frontal End: Undamaged (`Front Normal`) | Impact Compressed (`Front Crushed`) | Component Fracture (`Front Breakage`)
  * Rear End: Undamaged (`Rear Normal`) | Impact Compressed (`Rear Crushed`) | Component Fracture (`Rear Breakage`)
* **System Evaluation:** Achieved a ~80% accuracy threshold on unseen validation data pools.

## Execution & Environment Setup

### 1. Dependency Alignment
Initialize your localized virtual workspace environment and install the core architecture libraries by running:
```commandline
pip install -r requirements.txt
```

### 2. Initializing the Architecture (Two-Step Process)
Because this application is built using a decoupled architecture, you must initialize the backend calculation engine and the frontend interface in **two separate terminal windows**:

#### Window A: Initialize the FastAPI Prediction Server
Navigate to the root directory and spin up the model worker instance:
```commandline
uvicorn server:app --reload
```
*The server will boot up and listen for image payloads at `http://127.0.0.1:8000`.*

#### Window B: Initialize the Streamlit UI Dashboard
Open a new terminal tab, activate your virtual environment, and launch the user interface client:
```commandline
streamlit run app.py
```
