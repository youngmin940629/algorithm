from collections import deque

N, K = map(int, input().split())
arr = deque()
for i in range(N):
    arr.append(i+1)
result = []
count = N
index = 0
for i in range(N):
    index += (K - 1)
    if index >= count:
        index = index % count
    result.append(arr[index])
    del arr[index]
    count -= 1
result = ', '.join(map(str, result))
print(f"<{result}>")
