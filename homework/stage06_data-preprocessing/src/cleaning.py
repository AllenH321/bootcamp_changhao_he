# cleaning.py  (Stage 06 - match professor's example)

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler


def fill_missing_median(df, columns=None):
    df_copy = df.copy()
    if columns is None:
        columns = df_copy.select_dtypes(include=np.number).columns
    for col in columns:
        df_copy[col] = df_copy[col].fillna(df_copy[col].median())
    return df_copy


def drop_missing(df, columns=None, threshold=None):

    df_copy = df.copy()

    if threshold is None:
        return df_copy.dropna(subset=columns)

    # compute required non-null count
    N = len(columns) if columns is not None else df_copy.shape[1]
    keep_at_least = int(np.ceil(threshold * N)) if (0 < threshold <= 1) else int(threshold)
    return df_copy.dropna(thresh=keep_at_least, subset=columns)


def normalize_data(df, columns=None, method='minmax'):
    """
    Scale numeric data:
      - method='minmax' → MinMaxScaler() to [0,1]
      - method!='minmax' → StandardScaler() (z-score)
    """
    df_copy = df.copy()
    if columns is None:
        columns = df_copy.select_dtypes(include=np.number).columns
    if len(columns) == 0:
        return df_copy

    scaler = MinMaxScaler() if method == 'minmax' else StandardScaler()
    df_copy[columns] = scaler.fit_transform(df_copy[columns].to_numpy(dtype=float))
    return df_copy


def correct_column_types(df):
    """
    Clean common messy fields:
      - 'price': strip $ and commas → float
      - 'date_str': parse to datetime and store in/overwrite 'date'
      - 'category': lowercase → pandas 'category'
    """
    df_copy = df.copy()

    if 'price' in df_copy.columns:
        s = df_copy['price'].astype(str).str.replace(r'[\$,]', '', regex=True)
        df_copy['price'] = pd.to_numeric(s, errors='coerce')

    if 'date_str' in df_copy.columns:
        df_copy['date'] = pd.to_datetime(df_copy['date_str'], errors='coerce')

    if 'category' in df_copy.columns:
        df_copy['category'] = df_copy['category'].astype(str).str.strip().str.lower().astype('category')

    return df_copy
