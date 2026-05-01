import time
import functools

def timer(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        duration = end_time - start_time
        print(f"Function {func.__name__} took {duration:.4f}s")
        return result
    return wrapper
@timer
def exercise28(seconds: float = 1.5):
    time.sleep(seconds)
if __name__ == "__main__":
    exercise28(1.5)
