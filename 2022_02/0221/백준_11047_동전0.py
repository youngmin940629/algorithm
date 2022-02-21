N, K = map(int, input().split())
coin = []
for _ in range(N):
    coin.append(int(input()))
result = 0
for i in range(N-1, -1, -1):
    if K == 0:
        break
    if coin[i] <= K:
        result += (K // coin[i])
        K = K  % coin[i]
print(result)
