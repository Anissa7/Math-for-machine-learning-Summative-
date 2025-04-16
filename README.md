# 📊 Linear Regression Prediction System

This project presents a complete machine learning pipeline that predicts a target variable using linear regression, deployed via a FastAPI backend and accessed through a custom-designed web interface.

---

## 🧠 Project Overview
- **Mission-based Use Case:** Predicts a public health indicator using year and numerical feature inputs .
- **Trained Models:**
  - Linear Regression ✅
  - Decision Tree ✅
  - Random Forest ✅
- **Evaluation:**
  - Metrics: Mean Squared Error, R² Score
  - Visualization: Loss curves for training & test sets
- **Best Model:** Exported and used in deployment.

---

## 📁 Folder Structure
```
linear_regression_model/
├── summative/
│   ├── linear_regression/
│   │   ├── multivariate.ipynb          # Notebook with model training & evaluation
│   │   ├── best_model.pkl              # Saved best-performing model
│   ├── API/
│   │   ├── prediction.py               # FastAPI backend
│   │   ├── requirements.txt            # All dependencies
│   ├── WebApp/
│   │   ├── index.html                  # Modern web interface for predictions
```

---

## 🚀 How to Run the Project

### 1. 🔍 Model Notebook
Open and run all cells in:
```
summative/linear_regression/multivariate.ipynb
```
- Explore model training, evaluation, and comparisons
- View performance metrics and exported model

### 2. ⚙️ FastAPI Backend
```bash
cd summative/API
pip install -r requirements.txt
uvicorn prediction:app --reload
```
Then open:
```
http://127.0.0.1:8000/docs
```
Use Swagger UI to test the `/predict` endpoint.

### 3. 🌐 Web App Interface
Open this file in your browser:
```
summative/WebApp/index.html
```
- Enter values for `YEAR_DISPLAY` and `Numeric`
- Click **Predict**
- View model results instantly

---

## 📹 Video Demo
- **YouTube Link:** [🔗 Watch the full 5-min demo](https://your-youtube-link.com)
- Includes:
  - Swagger UI API test
  - Web app prediction
  - Model explanation (Linear Regression, Random Forest, Decision Tree)

---

## 🌍 Live API (Optional)
- [https://your-api-url.onrender.com/docs](https://your-api-url.onrender.com/docs) _(if deployed)_

---

## ✅ Submission Notes
- This project uses a real dataset aligned with a real-world mission
- Avoided generic house price prediction use case as instructed
- Met all technical and UI requirements for the summative assignment

---

Created with ❤️ by Anissa Ouedraogo

