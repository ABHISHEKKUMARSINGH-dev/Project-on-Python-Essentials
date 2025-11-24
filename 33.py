s = float(input("Enter s: "))
terms = int(input("Enter number of terms: "))

zeta = 0.0
n = 1

while n <= terms:
    zeta += 1 / (n ** s)
    n += 1

print("Zeta approximation =", zeta)
