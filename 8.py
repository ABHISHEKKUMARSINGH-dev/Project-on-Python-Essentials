import time
import sys

def is_automorphic(n):
    start_time = time.time()
    
    if not isinstance(n, int):
        n = int(n)

    if n < 0:
        is_automorphic_bool = False
    elif n == 0:
        is_automorphic_bool = True
    else:
        n_squared = n * n
        num_digits = len(str(n))
        magnitude = 10 ** num_digits
        
        is_automorphic_bool = (n_squared % magnitude == n)

    time_taken = time.time() - start_time
    storage_used = sys.getsizeof(n) + sys.getsizeof(is_automorphic_bool)
    return is_automorphic_bool, time_taken, storage_used

def run_test(n):
    result, time_taken, storage_used = is_automorphic(n)
    is_automorphic_str = "Automorphic Number" if result else "Not an Automorphic Number"
    print("-" * 40)
    print(f"Number: {n}")
    print(f"Classification: {is_automorphic_str}")
    print(f"Time Taken: {time_taken:.8f} seconds")
    print(f"Storage Used: {storage_used} bytes")

run_test(5)
run_test(6)
run_test(25)
run_test(76)
run_test(376)
run_test(10)