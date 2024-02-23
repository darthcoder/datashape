import pandas as pd
import openpyxl
import os

def load_data(filename):
    """Loads data from a CSV or Excel file.

    Args:
        filename (str): Path to the file.

    Returns:
        pandas.DataFrame: The loaded DataFrame.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        PermissionError: If the user lacks permissions to read the file.
        ValueError: If the file format is unsupported.
        IOError: For other general input/output errors.
    """

    if not os.path.exists(filename):
        raise FileNotFoundError(f"File not found: {filename}")

    try:
        if filename.endswith('.csv'):
            return pd.read_csv(filename)
        elif filename.endswith('.xlsx') or filename.endswith('.xls'):
            return pd.read_excel(filename)
        else:
            raise ValueError("Unsupported file format. Supported formats: CSV, XLSX, XLS")
    except PermissionError:
        raise PermissionError(f"You don't have permission to read the file: {filename}")
    except (IOError, OSError) as e:  # Catching other potential I/O errors
        raise IOError(f"Error loading file: {filename} - {e}") 
    
def save_report(df, filename):
    """Saves a DataFrame as a CSV file.

    Args:
        df (pandas.DataFrame): The DataFrame to save.
        filename (str): Path to the output file.
    """
    df.to_csv(filename, index=False)  



