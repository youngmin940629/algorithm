N = int(input())
arr = list(map(int, input().split()))
tmp = arr[:]
tmp.sort()
result = []
for i in range(N):
    idx = tmp.index(arr[i])
    result.append(idx)
    tmp[idx] = -1
print(*result)