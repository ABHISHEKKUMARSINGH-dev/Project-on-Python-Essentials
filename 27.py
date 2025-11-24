import time
import sys
import math

def is_perfect_power(n):
    start_time = time.time()
    
    if not isinstance(n, int) or n < 0:
        time_taken = time.time() - start_time
        storage_used = sys.getsizeof(n)
        return False, time_taken, storage_used
        
    if n == 1:
        time_taken = time.time() - start_time
        storage_used = sys.getsizeof(n)
        return True, time_taken, storage_used

    # Maximum possible exponent b (since 2^b <= n, max b is log2(n))
    max_exponent = math.floor(math.log2(n))
    is_perfect_power_bool = False
    
    # Iterate through possible exponents (b) from 2 up to max_exponent
    for b in range(2, max_exponent + 1):
        # Calculate the b-th root of n (n^(1/b))
        a_float = n ** (1.0 / b)
        
        # Check if the root is an integer (a)
        a_int = round(a_float)
        
        # Check if a_int raised to the power of b exactly equals n
        if a_int ** b == n:
            is_perfect_power_bool = True
            break
            
    time_taken = time.time() - start_time
    storage_used = sys.getsizeof(n) + sys.getsizeof(max_exponent) + sys.getsizeof(is_perfect_power_bool)
    return is_perfect_power_bool, time_taken, storage_used

def run_test(n):
    result, time_taken, storage_used = is_perfect_power(n)
    is_power_str = "is a Perfect Power (a^b)" if result else "is NOT a Perfect Power"
    
    print("-" * 40)
    print(f"Number: {n}")
    print(f"Classification: {is_power_str}")
    print(f"Time Taken: {time_taken:.8f} seconds")
    print(f"Storage Used: {storage_used} bytes")

run_test(8)    
run_test(16)   
run_test(27)   
run_test(10)
run_test(1000000)