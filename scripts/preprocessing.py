import pandas as pd
import os

def load_data(training_file: str, testing_file: str) -> tuple:
    """
    Load training and testing data from CSV files.

    Parameters:
    - training_file (str): Path to the training data CSV file.
    - testing_file (str): Path to the testing data CSV file.

    Returns:
    - tuple: A tuple containing the training DataFrame and the testing DataFrame.
    """
    if not os.path.isfile(training_file):
        raise FileNotFoundError(f"Training file '{training_file}' does not exist.")
    if not os.path.isfile(testing_file):
        raise FileNotFoundError(f"Testing file '{testing_file}' does not exist.")

    training_data = pd.read_csv(training_file)
    testing_data = pd.read_csv(testing_file)

    print("Data loaded successfully.")
    return training_data, testing_data

def check_missing_values(data: pd.DataFrame) -> pd.Series:
    """
    Check for missing values in the DataFrame.

    Parameters:
    - data (pd.DataFrame): The DataFrame to check.

    Returns:
    - pd.Series: A Series indicating the count of missing values for each column.
    """
    missing_values = data.isnull().sum()
    return missing_values[missing_values > 0]  # Show only columns with missing values

def remove_duplicates(data: pd.DataFrame) -> pd.DataFrame:
    """
    Remove duplicate rows from the DataFrame.

    Parameters:
    - data (pd.DataFrame): The DataFrame to process.

    Returns:
    - pd.DataFrame: A DataFrame without duplicate rows.
    """
    initial_shape = data.shape
    data_cleaned = data.drop_duplicates()
    final_shape = data_cleaned.shape
    print(f"Removed {initial_shape[0] - final_shape[0]} duplicate rows.")
    return data_cleaned

def convert_date_column(data: pd.DataFrame, date_column: str) -> pd.DataFrame:
    """
    Convert a specified column to datetime format.

    Parameters:
    - data (pd.DataFrame): The DataFrame to modify.
    - date_column (str): The name of the column to convert.

    Returns:
    - pd.DataFrame: The DataFrame with the date column converted.
    """
    if date_column not in data.columns:
        raise ValueError(f"Column '{date_column}' not found in DataFrame.")

    data[date_column] = pd.to_datetime(data[date_column], errors='coerce')
    print(f"Column '{date_column}' converted to datetime.")
    return data