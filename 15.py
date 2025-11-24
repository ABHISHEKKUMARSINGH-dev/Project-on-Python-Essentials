import time
import sys

def count_divisors(n):
    start_time = time.time()  # Start timing
    divisor_count = 0
    
    for i in range(1, n + 1):
        if n % i == 0:
            divisor_count += 1
    
    time_taken = time.time() - start_time
    storage_used = sys.getsizeof(divisor_count) + sys.getsizeof(n)
    
    return divisor_count, time_taken, storage_used

# Example usage:
divisors, time_taken, storage_used = count_divisors(12)
print(f"Number of Divisors: {divisors}")
print(f"Time Taken: {time_taken} seconds")
print(f"Storage Used: {storage_used} bytes")