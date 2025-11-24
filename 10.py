import time
import sys
import math

def prime_factors(n):
    start_time = time.time()
    
    if not isinstance(n, int) or n <= 1:
        time_taken = time.time() - start_time
        storage_used = sys.getsizeof(n)
        return [], time_taken, storage_used

    factors = []
    
    # Handle the factor 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2
        
    # Handle odd factors from 3 up to sqrt(n)
    limit = math.isqrt(n)
    i = 3
    while i <= limit:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2
        
    # If n is a prime number greater than 2 (the final remaining factor)
    if n > 2:
        factors.append(n)

    time_taken = time.time() - start_time
    storage_used = sys.getsizeof(n) + sys.getsizeof(factors)
    return factors, time_taken, storage_used

def run_test(n):
    result, time_taken, storage_used = prime_factors(n)
    
    print("-" * 40)
    print(f"Number to Factor: {n}")
    print(f"Prime Factors: {result}")
    print(f"Time Taken: {time_taken:.8f} seconds")
    print(f"Storage Used: {storage_used} bytes")

run_test(12)
run_test(97)
run_test(13195)
run_test(600851475143)
run_test(1)