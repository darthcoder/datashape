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

# write a function to remove outliers from a dataframe
def remove_outliers(df, column_name, min_val, max_val):
    """Removes rows from a DataFrame that contain outliers.

    Args:
        df (pandas.DataFrame): The DataFrame to process.
        column_name (str): Name of the column to filter.
        min_val (int): Minimum accepted value.
        max_val (int): Maximum accepted value.

    Returns:
        pandas.DataFrame: The DataFrame with outliers removed.
    """

    return df[(df[column_name] >= min_val) & (df[column_name] <= max_val)]

# write a function to standardize a dataframe
def standardize(df):
    """Standardizes the data in a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame to process.

    Returns:
        pandas.DataFrame: The standardized DataFrame.
    """

    return (df - df.mean()) / df.std()
# write a function to normalize a dataframe
def normalize(df):
    """Normalizes the data in a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame to process.

    Returns:
        pandas.DataFrame: The normalized DataFrame.
    """

    return (df - df.min()) / (df.max() - df.min())
# write a function to encode categorical data
def encode_categorical(df, column_name):
    """Encodes categorical data in a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame to process.
        column_name (str): Name of the column to encode.

    Returns:
        pandas.DataFrame: The DataFrame with categorical data encoded.
    """

    return pd.get_dummies(df, columns=[column_name], drop_first=True)
# write a function to convert a date column to datetime
def convert_to_datetime(df, column_name):
    """Converts a column to a datetime data type.

    Args:
        df (pandas.DataFrame): The DataFrame to process.
        column_name (str): Name of the column to convert.

    Returns:
        pandas.DataFrame: The DataFrame with the column converted to datetime.
    """

    df[column_name] = pd.to_datetime(df[column_name])
    return df
# write a function to extract date features
def extract_date_features(df, date_column):
    """Extracts date features from a column.

    Args:
        df (pandas.DataFrame): The DataFrame to process.
        date_column (str): Name of the date column.

    Returns:
        pandas.DataFrame: The DataFrame with new date features.
    """

    df[date_column + '_year'] = df[date_column].dt.year
    df[date_column + '_month'] = df[date_column].dt.month
    df[date_column + '_day'] = df[date_column].dt.day
    return df
# write a function to remove a column from a dataframe
def remove_column(df, column_name):
    """Removes a column from a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame to process.
        column_name (str): Name of the column to remove.

    Returns:
        pandas.DataFrame: The DataFrame with the specified column removed.
    """

    return df.drop(column_name, axis=1)
# write a function to rename columns in a dataframe
def rename_column(df, old_name, new_name):
    """Renames a column in a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame to process.
        old_name (str): Current column name.
        new_name (str): New column name.

    Returns:
        pandas.DataFrame: The DataFrame with the column renamed.
    """

    return df.rename(columns={old_name: new_name})  
# write a function to create a new column in a dataframe
def create_column(df, column_name, value):
    """Creates a new column in a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame to process.
        column_name (str): Name of the new column.
        value (int, float, str, etc.): The value to populate the new column.

    Returns:
        pandas.DataFrame: The DataFrame with the new column added.
    """

    df[column_name] = value
    return df
# write a function to filter rows in a dataframe
def filter_rows(df, condition):
    """Filters rows in a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame to process.
        condition (str): The filtering condition.

    Returns:
        pandas.DataFrame: The filtered DataFrame.
    """

    return df.query(condition)
# write a function to sort rows in a dataframe
def sort_rows(df, column_name, ascending=True):
    """Sorts rows in a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame to process.
        column_name (str): Name of the column to sort by.
        ascending (bool, optional): Whether to sort in ascending order. Defaults to True.

    Returns:
        pandas.DataFrame: The sorted DataFrame.
    """

    return df.sort_values(by=column_name, ascending=ascending)
# write a function to reset the index of a dataframe
def reset_index(df):
    """Resets the index of a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame to process.

    Returns:
        pandas.DataFrame: The DataFrame with the index reset.
    """

    return df.reset_index(drop=True)
# write a function to drop duplicate rows from a dataframe
def drop_duplicates(df, column_names):
    """Drops duplicate rows from a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame to process.
        column_names (list): Names of columns to consider when identifying duplicates.

    Returns:
        pandas.DataFrame: The DataFrame with duplicate rows removed.
    """

    return df.drop_duplicates(subset=column_names)
# write a function to perform a groupby operation in a dataframe
def group_data(df, column_name):
    """Groups data in a DataFrame by a specified column.

    Args:
        df (pandas.DataFrame): The DataFrame to process.
        column_name (str): Name of the column to group by.

    Returns:
        pandas.core.groupby.DataFrameGroupBy: The grouped DataFrame.
    """

    return df.groupby(column_name)
# write a function to aggregate data in a dataframe
def aggregate_data(grouped_data, aggregation):
    """Aggregates grouped data.

    Args:
        grouped_data (pandas.core.groupby.DataFrameGroupBy): The grouped DataFrame.
        aggregation (dict): The aggregation to perform (e.g., {'column_name': 'mean'}).

    Returns:
        pandas.DataFrame: The aggregated data.
    """

    return grouped_data.agg(aggregation)

