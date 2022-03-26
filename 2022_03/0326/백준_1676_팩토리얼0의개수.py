N = int(input())
dp = [0] * 501
dp[0] = dp[1] = 1
for i in range(2, N+1):
    dp[i] = dp[i-1] * i
result = 0
factorial = dp[N]
while True:
    if factorial % 10 == 0:
        result += 1
        factorial = factorial // 10
    else:
        break
print(result)