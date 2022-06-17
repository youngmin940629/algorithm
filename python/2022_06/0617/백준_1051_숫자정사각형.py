n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(input()))
min_check = min(n, m)
answer = 0
for i in range(n):
    for j in range(m):
        for k in range(min_check):
            if ((i + k) < n) and ((j + k) < m) and (arr[i][j] == arr[i][j + k] == arr[i + k][j] == arr[i + k][j + k]):
                answer = max(answer, (k + 1)**2)
print(answer)