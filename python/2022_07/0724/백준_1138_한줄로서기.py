n = int(input())
h = list(map(int, input().split()))
result = [0] * n
for i in range(1, n+1):
    t = h[i-1]
    cnt = 0
    for j in range(n):
        if cnt == t and result[j] == 0:
            result[j] = i
            break
        elif result[j] == 0:
            cnt += 1
print(*result)