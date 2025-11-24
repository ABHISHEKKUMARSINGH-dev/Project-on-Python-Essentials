n = int(input("Enter n: "))

# dp[i] = number of partitions of i
dp = [0] * (n + 1)
dp[0] = 1

num = 1
while num <= n:
    i = num
    while i <= n:
        dp[i] += dp[i - num]
        i += 1
    num += 1

print("Number of partitions p(n):", dp[n])
