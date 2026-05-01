import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Function {func.__name__!r} executed in {end - start:.10f}s")
        return result
    return wrapper
if __name__ == "__main__":
    @timer
    def test(n):
        time.sleep(n)

    test(2.1)
