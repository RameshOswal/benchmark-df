import time

NUM_ROWS = 100_000_000

def timer_decorator(func):
    """Decorator to measure function runtime"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds to run")
        return result
    return wrapper 