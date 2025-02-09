import pandas as pd
import numpy as np
from helpers.time_decorator import timer_decorator, NUM_ROWS

def create_dataframe():
    """Create a Pandas DataFrame with sample data"""
    data = {
        "col1": np.random.randn(NUM_ROWS),
        "col2": np.random.randn(NUM_ROWS),
    }
    return pd.DataFrame(data)

@timer_decorator
def process_dataframe(df):
    """Apply operations on Pandas DataFrame"""
    return df["col1"].mean() + df["col2"].mean()

