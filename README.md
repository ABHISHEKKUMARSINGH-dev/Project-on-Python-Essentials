# Number Theory & Algorithms Collection

A comprehensive set of **34 Python modules** dealing with the properties of integers, prime numbers, cryptographic primitives, and computational number theory; this repository covers topics from basic manipulation of digits up to advanced probabilistic algorithms and discrete mathematics sequences.

Overview ????

This project shows algorithmic skills in Python by paying attention to mathematical rigor, efficiency, and clarity of the code.

**Performance Profiling:** The majority of scripts have automatic `time` and `sys` (or `tracemalloc`) profiling to measure execution speed and memory overhead.

* **Standard Library Only:** All solutions run using native Python libraries (`math`, `time`, `sys`, `random`), ensuring zero external dependencies.

---

Complete Algorithm Catalog
| File | Function / Algorithm | Description | Concept |
| :--- | :--- | :--- | :--- |
| `1.py` | `factorial(n)` | Computes n! iteratively. | Combinatorics |
| `2.py` | `is_palindrome(n)` | Checks if n reads the same forwards and backwards. | String Manipulation |
| `3.py` | `mean_of_digits(n)` | Returns the arithmetic mean of all digits in n. | Statistics |
| `4.py` | `digital_root(n)` | Recursively sum the digits until only a single digit remains. | Congruence Formula |
| `5.py` | `is_abundant(n)` | Checks if sum of proper divisors > n. | Divisor Sum |
| `6.py` | `is_deficient(n)` | Checks if sum of proper divisors < n. | Divisor Sum |
| `7.py` | `is_harshad(n)` | Checks if n is divisible by the sum of its digits. | Niven Numbers |
| `8.py` | `is_automorphic(n)` | Checks if n^2 ends with the digits of n. | Modular Arithmetic |
| `9.py` | `is_pronic(n)` | Returns whether n is the product of consecutive integers k(k+1). | Oblong Numbers |
| `10.py` | `prime_factors(n)` | Returns a list of all prime factors using trial division. | Factorization |
| `11.py` | `count_distinct_factors` | Counts unique prime factors of n. | Prime Factorization |
| `12.py` | `is_prime_power(n)` | Returns whether n = p^k where p is prime and k ≥ 1. | Exponentiation |
| `13.py` | `is_mersenne_prime(p)` | Checks whether 2^p - 1 is prime, using bitwise shifts. | Mersenne Primes |
| `14.py` | `twin_primes(limit)` | Generates pairs (p, p+2) up to a limit. | Twin Prime Conjecture |
| `15.py` | `count_divisors(n)` | Computes the total number of divisors. | Divisor Function |
| `16.py` | `aliquot_sum(n)` | Sum of proper divisors (used for Perfect numbers). | Aliquot Sequence |
| `17.py` | `are_amicable(a, b)` | Checks if two numbers' aliquot sums equal each other. | Amicable Pairs |
| `18.py` | `multiplicative_persistence`| Counts steps to reach a single digit via multiplication. | Persistence |
| `19.py` | `is_highly_composite` | Tests if n has more divisors than any smaller positive integer. | HCN |
| `20.py` | `modular_exponentiation` | Efficiently calculates (b^e) mod m. | Cryptography |
| `21.py` | `mod_inverse(a, m)` | Finds x such that ax = 1 mod m using Extended GCD. | Euclidean Algorithm |
| `22.py` | `crt(remainders, moduli)` | Solves system of congruences using Chinese Remainder Theorem. | System of Congruences |
| `23.py` | `is_quadratic_residue` | Checks if x^2 = a mod p is solvable via Euler's Criterion. | Quadratic Reciprocity |
| `24.py` | `order_mod(a, n)` | Computes the multiplicative order of a modulo n. | Group Theory |
| `25.py` | `is_fibonacci_prime(n)` | Checks if a number is both Fibonacci and Prime. | Prime Constants |
| `26.py` | `lucas_sequence(n)` | Returns Lucas numbers (like Fib, starts 2, 1). | Recurrence Relations |
| `27.py` | `is_perfect_power(n)` | Checks if n = a^b where a > 0, b > 1. | Exponential Equations |
| `28.py` | `collatz_length(n)` | Returns steps for n to reach 1 (3n+1 problem). | Unsolved Problems |
| `29.py` | `polygonal_number(s, n)` | Calculates the n-th s-gonal number (Triangular, Pentagonal).| Geometric Numbers |
| `30.py` | `is_carmichael(n)` | Returns whether composite n satisfies a^(n-1) = 1 mod n. | Pseudoprimes |
| `31.py` | `miller_rabin(n)` | Given a large integer, returns probably prime result. | Randomized Algo |
| `32.py` | `pollards_rho(n)` | Integer factorization using Floyd's cycle-finding logic. | Sub-exponential |

| `33.py` | `riemann_zeta(s)` | Approximates Zeta(s) via partial summation. | Numerical Analysis |

| `34.py` | `partition_function(n)` | Computes p(n) - the number of ways to write n as a sum using DP. | Dynamic Programming |

---

Implementation Highlights & Theory

Chinese Remainder Theorem (File 22)
Crucial for RSA decryption performance optimization. The function solves a system of congruences x = r_i (mod m_i) by constructing the solution using modular inverses of partial products N_i = N/m_i.
```python
def crt(remainders, moduli):
# Calculate N (product of all moduli)
# Solve for x using: sum(r_i * N_i * inverse(N_i, m_i)) % N

y_i = mod_inverse(N_i, m_i)

total += r_i * N_i * y_i

Collatz Conjecture (File 28)

The function here implements the rules of the famous "3n + 1" problem; for any positive integer n, if even, divide by 2, otherwise multiply by 3 and add 1. This function will keep track of the trajectory length or stopping time.

Carmichael Numbers (File 30)

Identifies "pseudoprimes" that foil the Fermat primality test. The function checks first that n is composite, then that a^(n-1) = 1 mod n for all a coprime to n.

Pollard's Rho Algorithm (File 32)


Finds a nontrivial factor of a composite integer n more quickly than trial division, using a randomized function f(x) = x^2 + c (mod n) to find cycles.

Setup & Usage 
Clone the repository: 
Bash 
git clone https://github.com/ABHISHEKKUMARSINGH-dev/ProjectonPythonEssentials.git
Run a particular file: All files are self-contained. Run them directly using Python:
Bash 
python 26.py 
Example Output: 
Python 3.x
No packages are required beyond the standard libraries: math, sys, time, random.
