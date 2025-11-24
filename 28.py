import time
import sys

def collatz_length(n):
    start_time = time.time()
    
    if not isinstance(n, int) or n < 1:
        time_taken = time.time() - start_time
        storage_used = sys.getsizeof(n)
        return 0, time_taken, storage_used

    length = 0
    temp_n = n
    
    while temp_n != 1:
        if temp_n % 2 == 0:
            temp_n //= 2
        else:
            temp_n = 3 * temp_n + 1
        length += 1
        
    time_taken = time.time() - start_time
    storage_used = sys.getsizeof(n) + sys.getsizeof(length)
    return length, time_taken, storage_used

def run_test(n):
    result, time_taken, storage_used = collatz_length(n)
    
    print("-" * 40)
    print(f"Number (n): {n}")
    print(f"Steps to reach 1: {result}")
    print(f"Execution Time: {time_taken:.8f} seconds")
    print(f"Storage Used: {storage_used} bytes")

run_test(6)
run_test(27)
run_test(100)
run_test(1)