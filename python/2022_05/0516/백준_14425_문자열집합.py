N, M = map(int, input().split())
result = 0
S = []
for _ in range(N):
    S.append(input())
for _ in range(M):
    word = input()
    if word in S:
        result += 1
print(result)