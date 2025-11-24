n = int(input("Enter number to test primality: "))
k = int(input("Enter number of rounds: "))

if n < 2:
    print("Composite")
    exit()
if n in (2, 3):
    print("Prime")
    exit()
if n % 2 == 0:
    print("Composite")
    exit()

d = n - 1
r = 0
while d % 2 == 0:
    d //= 2
    r += 1


bases = [2, 3, 5, 7, 11, 13, 17]
is_probably_prime = True
base_index = 0

for _ in range(k):
    a = bases[base_index]
    base_index += 1
    if a >= n - 1:
        break

    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        continue

    composite_flag = True
    for _ in range(r - 1):
        x = (x * x) % n
        if x == n - 1:
            composite_flag = False
            break

    if composite_flag:
        is_probably_prime = False
        break

if is_probably_prime:
    print("Probably Prime")
else:
    print("Composite")
