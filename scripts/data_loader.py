import pandas as pd

def load_data_finance(file_path):

    """Codeium docs
    Loads a CSV file from the given file path, parsing the Date column as a datetime.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: A pandas DataFrame containing the loaded data.
    """
    
    return pd.read_csv(file_path, parse_dates=["Date"]) 

def load_data(file_path):

    """Codeium docs
    Loads a CSV file from the given file path, parsing the Date column as a datetime.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: A pandas DataFrame containing the loaded data.
    """
    
    return pd.read_csv(file_path) 