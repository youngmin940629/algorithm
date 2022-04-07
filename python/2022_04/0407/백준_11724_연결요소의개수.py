from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)
q = deque()
visited = [0] * (N+1)

def bfs():
    while q:
        node = q.popleft()
        visited[node] = 1
        for next in arr[node]:
            if not visited[next]:
                q.append(next)
result = 0
for i in range(1, N+1):
    if not visited[i]:
        if not arr[i]:
            result += 1
            visited[i] = 1
        else:
            result += 1
            q.append(i)
            bfs()
print(result)