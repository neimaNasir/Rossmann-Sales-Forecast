import logging
import os
import pandas as pd

# Create logs directory if it does not exist
if not os.path.exists('logs'):
    os.makedirs('logs')

# Set up logging to a file in the logs directory
log_file_path = os.path.join('logs', 'eda.log')
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger('EDA_Logger')

def log_error(message: str) -> None:
    """
    Log an error message.

    Parameters:
    - message (str): The error message to log.
    """
    logger.error(message)

def log_warning(message: str) -> None:
    """
    Log a warning message.

    Parameters:
    - message (str): The warning message to log.
    """
    logger.warning(message)

def log_debug(message: str) -> None:
    """
    Log a debug message.

    Parameters:
    - message (str): The debug message to log.
    """
    logger.debug(message)

def load_data(training_file: str, testing_file: str) -> tuple:
    """
    Load training and testing data from CSV files.

    Parameters:
    - training_file (str): Path to the training data CSV file.
    - testing_file (str): Path to the testing data CSV file.

    Returns:
    - tuple: A tuple containing the training DataFrame and the testing DataFrame.
    """
    training_data = pd.read_csv(training_file)
    testing_data = pd.read_csv(testing_file)

    logger.info(f'Loaded training data with {training_data.shape[0]} rows and {training_data.shape[1]} columns')
    logger.info(f'Loaded testing data with {testing_data.shape[0]} rows and {testing_data.shape[1]} columns')
    return training_data, testing_data

def check_missing_values(data: pd.DataFrame) -> pd.Series:
    """
    Check for missing values in the dataframe.

    Parameters:
    - data (pd.DataFrame): The DataFrame to check.

    Returns:
    - pd.Series: A Series indicating the count of missing values for each column.
    """
    missing_values = data.isnull().sum()
    logger.info(f'Missing values found: {missing_values}')
    return missing_values