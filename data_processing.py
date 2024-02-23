import pandas as pd


def handle_missing_values(df, method="mean"):
    """Fills missing values in a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame to process.
        method (str, optional): Method for filling missing values. 
                                Defaults to 'mean'. Options: 'mean', 'median', 
                                'ffill' (forward fill), 'bfill' (back fill), or a custom value.

    Returns:
        pandas.DataFrame: The DataFrame with missing values filled.
    """

    if method == "mean":
        return df.fillna(df.mean())
    elif method == "median":
        return df.fillna(df.median())
    elif method in ["ffill", "bfill"]:
        return df.fillna(method=method)
    elif isinstance(method, (int, float)):  # Allow a custom fill value
        return df.fillna(method)
    else:
        raise ValueError(f"Invalid missing value handling method: {method}")


def clean_text_column(df, column_name):
    """Performs basic text cleaning on a specified column.

    Args:
        df (pandas.DataFrame): The DataFrame to process.
        column_name (str): Name of the text column.

    Returns:
        pandas.DataFrame: The modified DataFrame.
    """

    df[column_name] = df[column_name].str.strip()    # Remove leading/trailing whitespace
    df[column_name] = df[column_name].str.lower()  # Convert to lowercase (optional)
    return df


def change_data_type(df, column_name, new_type):
    """Changes the data type of a specified column.

    Args:
        df (pandas.DataFrame): The DataFrame.
        column_name (str): Name of the column.
        new_type (str): The desired data type (e.g., 'int64', 'float64', 'str').

    Returns:
        pandas.DataFrame: The modified DataFrame.
    """

    df[column_name] = df[column_name].astype(new_type)
    return df

