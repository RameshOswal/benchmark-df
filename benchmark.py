import time
import sys

def benchmark(ops_module):
    print(f"Running benchmarks for {ops_module.__name__}")
    
    start = time.time()
    df = ops_module.create_dataframe()
    end = time.time()
    print(f"Dataframe creation time: {end - start:.6f}s")

    start = time.time()
    result = ops_module.process_dataframe(df)
    end = time.time()
    print(f"Dataframe processing time: {end - start:.6f}s")

if __name__ == "__main__":
    module_name = sys.argv[1]
    if module_name == "pandas":
        import pandas_ops as ops
    elif module_name == "polars":
        import polars_ops as ops
    else:
        raise ValueError("Invalid module name. Use 'pandas' or 'polars'.")

    benchmark(ops)

