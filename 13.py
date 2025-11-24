import time
import sys

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_mersenne_prime(p):
    start_time = time.time()  # Start timing
    
    if not is_prime(p):
        return False, 0, 0
    
    mersenne_number = (1 << p) - 1  # This is 2^p - 1
    
    if mersenne_number <= 1:
        return False, 0, 0
    
    # Check if mersenne_number is prime
    if is_prime(mersenne_number):
        time_taken = time.time() - start_time
        storage_used = sys.getsizeof(mersenne_number)
        return True, time_taken, storage_used
    
    time_taken = time.time() - start_time
    storage_used = sys.getsizeof(mersenne_number)
    return False, time_taken, storage_used

result, time_taken, storage_used = is_mersenne_prime(3)
print(f"Is Mersenne Prime: {result}")
print(f"Time Taken: {time_taken} seconds")
print(f"Storage Used: {storage_used} bytes")