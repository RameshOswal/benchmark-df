import polars as pl
import numpy as np
from helpers.time_decorator import timer_decorator, NUM_ROWS

@timer_decorator
def create_dataframe():
    """Create a Polars DataFrame with sample data"""
    data = {
        "col1": np.random.randn(NUM_ROWS).tolist(),
        "col2": np.random.randn(NUM_ROWS).tolist(),
    }
    return pl.DataFrame(data)

@timer_decorator
def process_dataframe(df):
    """Apply operations on Polars DataFrame"""
    return df["col1"].mean() + df["col2"].mean()

