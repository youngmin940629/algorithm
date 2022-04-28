from collections import deque

u, v = map(int, input().split())
arr = [i for i in range(101)]
for _ in range(u):
    a, b = map(int, input().split())
    arr[a] = b

for _ in range(v):
    a, b = map(int, input().split())
    arr[a] = b
result = 0
q = deque()
q.append((1,0))
visited = [0] * 101
while q:
    x, cnt = q.popleft()
    if x == 100:
        result = cnt
        break
    for dir in range(1,7):
        if x + dir <= 100:
            next = arr[x + dir]
        if next <= 100:
            if not visited[next]:
                visited[next] = cnt+1
                q.append((next,cnt+1))
            elif visited[next] > cnt+1:
                visited[next] = cnt+1
                q.append((next, cnt+1))
print(result)