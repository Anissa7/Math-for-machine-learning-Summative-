# data_preprocessing.py
import pandas as pd

def load_and_preprocess(csv_path: str) -> pd.DataFrame:
    """
    Loads and preprocesses the dataset.
    
    Parameters:
    - csv_path (str): Path to the CSV file.
    
    Returns:
    - pd.DataFrame: Cleaned DataFrame ready for modeling.
    """
    # Load dataset
    data = pd.read_csv(csv_path)

    # Convert 'YEAR (DISPLAY)' to numeric, coercing errors to NaN
    data['YEAR (DISPLAY)'] = pd.to_numeric(data['YEAR (DISPLAY)'], errors='coerce')

    # Extract numeric value from 'Value' column using regex
    # Adjust regex as needed for your particular dataset
    data['Value'] = data['Value'].str.extract(r'(\d+\.?\d*)').astype(float)

    # Drop rows with missing values in the relevant columns
    cleaned_data = data.dropna(subset=['YEAR (DISPLAY)', 'Numeric', 'Value'])
    
    return cleaned_data

if __name__ == "__main__":
    # Quick test of the preprocessing function
    df = load_and_preprocess('health_indicators_bfa.csv')
    print(df.head())
    print("Data shape after cleaning:", df.shape)
