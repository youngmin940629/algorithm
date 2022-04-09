import math

n = int(input())

dp = [0] * (n+1)
dp[0] , dp[1] = 0, 1

i = 2
while i <= n:
    if int(i**0.5)**2 == i:
        dp[i] = 1
    else:
        dp[i] = i
    i += 1

for i in range(2,n+1):
    j = 1
    while j <= int(math.sqrt(i)):
        dp[i] = min(dp[i], dp[j * j] + dp[i-j*j])
        j += 1
print(dp[n])