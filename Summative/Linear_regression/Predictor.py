# predictor.py
import pandas as pd
import joblib

def load_model(model_path: str = "best_model.pkl"):
    """
    Load the saved model from the specified path.
    
    Parameters:
    - model_path (str): Path to the saved model file.
    
    Returns:
    - model: Loaded model object.
    """
    return joblib.load(model_path)

def predict(input_data: dict) -> float:
    """
    Make a prediction using the saved best model.
    
    Parameters:
    - input_data (dict): Dictionary containing input features with keys ['YEAR (DISPLAY)', 'Numeric'].
    
    Returns:
    - float: The predicted value.
    """
    # Define feature order based on training data
    feature_names = ['YEAR (DISPLAY)', 'Numeric']
    sample_input = pd.DataFrame([input_data], columns=feature_names)
    
    # Load model and make prediction
    model = load_model()
    prediction = model.predict(sample_input)
    return prediction[0]

if __name__ == "__main__":
    # Quick test using sample input data
    sample = {"YEAR (DISPLAY)": 2023, "Numeric": 50}
    result = predict(sample)
    print("Prediction:", result)

# predictor.py
import pandas as pd
import joblib

def load_model(model_path: str = "best_model.pkl"):
    """
    Load the saved model from the specified path.
    
    Parameters:
    - model_path (str): Path to the saved model file.
    
    Returns:
    - model: Loaded model object.
    """
    return joblib.load(model_path)

def predict(input_data: dict) -> float:
    """
    Make a prediction using the saved best model.
    
    Parameters:
    - input_data (dict): Dictionary containing input features with keys ['YEAR (DISPLAY)', 'Numeric'].
    
    Returns:
    - float: The predicted value.
    """
    # Define feature order based on training data
    feature_names = ['YEAR (DISPLAY)', 'Numeric']
    sample_input = pd.DataFrame([input_data], columns=feature_names)
    
    # Load model and make prediction
    model = load_model()
    prediction = model.predict(sample_input)
    return prediction[0]

if __name__ == "__main__":
    # Quick test using sample input data
    sample = {"YEAR (DISPLAY)": 2023, "Numeric": 50}
    result = predict(sample)
    print("Prediction:", result)

    try:
        model = load_model()
    except Exception as e:
        print("Model loading failed:", e)
        raise

