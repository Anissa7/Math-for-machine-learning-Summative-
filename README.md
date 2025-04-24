# 📊 Linear Regression Prediction System

This project presents a complete machine learning pipeline that predicts a target variable using linear regression. It is deployed via a FastAPI backend and accessed through a custom-designed web interface.

---
## 📊 Dataset Description

The dataset contains public health metrics for Burkina Faso from **year X** to **year Y**, with features including `YEAR_DISPLAY` and `Numeric` (e.g., sanitation index, health spending).

➕ **Data Volume**: ~X rows, ~Y columns  
➕ **Data Variety**: Includes numerical and temporal features.

**Target Variable Predicted**: Number of malaria cases.

---

## 🧠 Project Overview

### **Mission-based Use Case**:
This project predicts a public health indicator based on input features such as year and a numerical metric (e.g., sanitation index).

### **Trained Models**:
- **Linear Regression** ✅
- **Decision Tree** ✅
- **Random Forest** ✅

### **Evaluation Metrics**:
- **Mean Squared Error (MSE)**
- **R² Score**
- **Visualization**: Loss curves for training & test sets.

### **Best Model**:
- **Best Performing Model**: **Random Forest Regressor** (lowest MSE)
- Exported and used for deployment in the FastAPI backend.

---

## 📁 Folder Structure
```
linear_regression_model/
├── summative/
│   ├── linear_regression/
│   │   ├── multivariate.ipynb          # Notebook with model training & evaluation
│   │   ├── best_model.pkl              # Saved best-performing model
│   ├── API/
│   │   ├── prediction.py               # FastAPI backend for prediction
│   │   ├── requirements.txt            # All dependencies for the API
│   ├── WebApp/
│   │   ├── index.html                  # Frontend interface for predictions
```

---

## 🚀 How to Run the Project

### 1. 🔍 **Model Notebook**  
Open and run all cells in the Jupyter notebook:
```
summative/linear_regression/multivariate.ipynb
```
- **Explore** model training, evaluation, and comparisons.
- **View** performance metrics and the exported best model.

### 2. ⚙️ **FastAPI Backend**  
Navigate to the API folder:
```bash
cd summative/API
pip install -r requirements.txt
uvicorn prediction:app --reload
```
Then open:
```
http://127.0.0.1:8000/docs
```
Use **Swagger UI** to test the `/predict` endpoint and interact with the FastAPI backend.

### 3. 🌐 **Web App Interface**  
Open the web app interface in your browser:
```
summative/WebApp/index.html
```
- Enter values for `YEAR_DISPLAY` and `Numeric`.
- Click **Predict** to get instant results.

---

## 📹 **Video Demo**  
Watch the full demo on YouTube:  
[🔗 **Watch the 3-minute video**](https://youtu.be/gDaG4W46WpI)

- **Demo Includes**:
  - Testing the API using Swagger UI
  - Using the web app interface for prediction
  - Explaining the model and evaluation process (Linear Regression, Decision Tree, Random Forest)

---

## 🌍 **Live API **  
Link to the API :http://127.0.0.1:8000/docs
If the API is deployed online, access it here:  
[**Live API Documentation**](https://your-api-url.onrender.com/docs)

---

## ✅ **Submission Notes**
- This project uses a **real dataset** aligned with a public health mission.
- Avoided generic use cases (e.g., house price prediction) as instructed.
- Met all technical and UI requirements for the summative assignment.

---

Created with ❤️ by **Anissa Ouedraogo**
