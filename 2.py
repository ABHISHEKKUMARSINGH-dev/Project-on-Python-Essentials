import time
import tracemalloc

def time_memory_profiler(func):
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = time.perf_counter()
        
        result = func(*args, **kwargs)
        
        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        execution_time = (end_time - start_time) * 1000
        
        print("-" * 40)
        print(f"Executing: {func.__name__}({args[0]})")
        print(f"Result: {result}")
        print(f"Execution time: {execution_time:.6f} ms")
        print(f"Current memory usage: {current / 1024:.2f} KB")
        print(f"Peak memory usage: {peak / 1024:.2f} KB")
        print("-" * 40)
        
        return result
    return wrapper

@time_memory_profiler
def is_palindrome(n):
    if n < 0:
        return False
    # Checks if the string representation of n is equal to its reverse [::-1]
    return str(n) == str(n)[::-1]

if __name__ == "__main__":
    print("Running palindrome checks with profiling...")
    is_palindrome(12321)
    is_palindrome(12345)
    is_palindrome(7)
    is_palindrome(987656789)
    is_palindrome(-101)