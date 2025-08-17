import pandas as pd
def get_summary_stats(df: pd.DataFrame) -> pd.DataFrame:
    return df.select_dtypes(include="number").describe().T