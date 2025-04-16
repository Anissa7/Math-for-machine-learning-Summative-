# model_training.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib


def train_models(data: pd.DataFrame):
    """
    Train Linear Regression, Decision Tree, and Random Forest models,
    then evaluate them using Mean Squared Error (MSE). Save the best-performing model.
    
    Parameters:
    - data (pd.DataFrame): Preprocessed dataset containing at least the columns:
                           'YEAR (DISPLAY)', 'Numeric', and 'Value'
    
    Returns:
    - dict: Dictionary with models' MSE values.
    - str: Name of the best model.
    """
    # Define features and target
    X = data[['YEAR (DISPLAY)', 'Numeric']]
    y = data['Value']
    
    # Split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train Linear Regression
    lr_model = LinearRegression()
    lr_model.fit(X_train, y_train)
    mse_lr = mean_squared_error(y_test, lr_model.predict(X_test))
    
    # Train Decision Tree Regressor
    dt_model = DecisionTreeRegressor(random_state=42)
    dt_model.fit(X_train, y_train)
    mse_dt = mean_squared_error(y_test, dt_model.predict(X_test))
    
    # Train Random Forest Regressor
    rf_model = RandomForestRegressor(random_state=42)
    rf_model.fit(X_train, y_train)
    mse_rf = mean_squared_error(y_test, rf_model.predict(X_test))
    
    # Compare models using MSE
    models_mse = {
        "Linear Regression": mse_lr,
        "Decision Tree": mse_dt,
        "Random Forest": mse_rf
    }
    
    best_model_name = min(models_mse, key=models_mse.get)
    best_model = {
        "Linear Regression": lr_model,
        "Decision Tree": dt_model,
        "Random Forest": rf_model
    }[best_model_name]
    
    # Save the best-performing model
    joblib.dump(best_model, "best_model.pkl")
    
    # Print and return results
    print(f"Mean Squared Errors: {models_mse}")
    print(f"Best Model: {best_model_name}")
    return models_mse, best_model_name

if __name__ == "__main__":
    # Run training pipeline and test
    data = load_and_preprocess('health_indicators_bfa.csv')
    mse_results, best_model = train_models(data)
