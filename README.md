# Machine Learning Regression Model, API, and Mobile App

## Overview
This project involves building a **linear regression model**, comparing its performance with **decision trees and random forests**, creating an **API using FastAPI** to serve predictions, and developing a **Flutter mobile application** to interact with the API.

---
## 📂 Repository Structure
```
linear_regression_model/
│
├── summative/
│   ├── linear_regression/
│   │   ├── multivariate.ipynb  # Jupyter Notebook for Model Training
│   ├── API/
│   │   ├── prediction.py       # FastAPI code for serving predictions
│   │   ├── requirements.txt    # Dependencies for running API
│   ├── FlutterApp/
│       ├── lib/
│       ├── android/
│       ├── ios/
│       ├── pubspec.yaml        # Flutter dependencies
```

---
## 📊 Task 1: Model Implementation
- **Dataset**: Fetched from Kaggle/Google Datasets (dataset used is mentioned in the notebook).
- **Models Implemented**:
  - Linear Regression (Gradient Descent Optimized)
  - Decision Tree
  - Random Forest
- **Comparison Metric**: Loss function analysis
- **Final Model Selection**: Based on best loss metric.
- **Loss Curve Visualization**: Plots for train/test data.
- **Saved Model**: The best-performing model is saved for API usage.

### Running the Notebook:
```sh
jupyter notebook multivariate.ipynb
```

---
## 🌐 Task 2: API Implementation (FastAPI)
- **Libraries Used**: `fastapi`, `pydantic`, `uvicorn`
- **POST Endpoint**: `/predict`
- **Input Validation**: Implemented using Pydantic for strict data type and range enforcement.
- **Hosting**: Deployed on **Render**.

### Running the API Locally:
```sh
pip install -r requirements.txt
uvicorn prediction:app --host 0.0.0.0 --port 8000
```

### API Testing:
- Open Swagger UI at: **[Public API URL]/docs**
- Example request:
```json
{
    "feature1": 10.5,
    "feature2": 3.7,
    "feature3": 42
}
```

---
## 📱 Task 3: Flutter Mobile App
- **Features**:
  - User input via text fields for model input variables.
  - A **Predict** button to send data to the API.
  - Display of predicted value or error message.
- **Dependencies**: Defined in `pubspec.yaml`.

### Running the Flutter App:
```sh
flutter run
```

---
## 🎥 Task 4: Video Demonstration
✅ **Link to YouTube Demo**: [Insert YouTube Link Here]
- Demonstrates:
  - API testing in Swagger UI.
  - Mobile app making predictions.
  - Model performance explanation (without code walkthrough).

---
## 🔗 Submission Checklist
✅ **GitHub Repository**: [Insert Repo Link Here]  
✅ **Public API Endpoint**: [Insert API Link Here]  
✅ **YouTube Video Demo**: [Insert Video Link Here]  
✅ **Instructions on running the project** provided.

---
## ❗ Important Notes
- **House price prediction is NOT used**, per assignment requirements.
- The **best model** was selected based on loss metric comparison.
- The **mobile app UI is structured properly** for usability.

---
### 🚀 Enjoy exploring the project! 🎯

