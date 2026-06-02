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
Initialize your workspace environment and install the required core libraries by executing:
```commandline
pip install -r requirements.txt
```

### 2. Launching the Local Server
Boot up the interactive browser dashboard via the Streamlit CLI engine:
```commandline
streamlit run app.py
```

