import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

def encode_categorical_columns(df, columns_to_convert, columns_to_drop):
    """
    Encode categorical columns using LabelEncoder.
    
    Args:
        df (pd.DataFrame): DataFrame containing the data.
        columns_to_convert (list): List of columns to encode.
        columns_to_drop (list): List of columns to drop.
        
    Returns:
        pd.DataFrame: DataFrame with encoded categorical columns.
    """
    # Drop rows with any NaN values
    df.dropna(inplace=True)

    # Drop duplicate rows and unnecessary columns
    df = df.drop(columns_to_drop, axis=1)
    df.drop_duplicates(inplace=True)

    # Convert specified columns to categorical
    df[columns_to_convert] = df[columns_to_convert].astype('category')
    
    label_encoder = LabelEncoder()

    for column in columns_to_convert:
        df[column] = label_encoder.fit_transform(df[column])
    
    return df

def split_data(df, target_column):
    """
    Split data into features and target variable.
    
    Args:
        df (pd.DataFrame): DataFrame containing the data.
        target_column (str): Name of the target column.
        
    Returns:
        pd.DataFrame, pd.Series: Features (X) and target variable (y).
    """
    y = df[target_column]
    x_df = df.drop([target_column], axis=1)
    
    return x_df, y
