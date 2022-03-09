N, K = map(int, input().split())
result = 1
divisor = 1
for i in range(K):
    result *= (N - i)
    divisor *= (K - i)

print(result // divisor)