from collections import deque

N, M, V = map(int, input().split())
arr = list([0] * (N+1) for _ in range(N+1))
for _ in range(M):
    x,y = map(int, input().split())
    arr[x][y] = arr[y][x] = 1
q = deque()
q.append(V)
dfs = [V]
bfs = [V]
visited = [0] * (N + 1)
visited[V] = 1
def DFS(n):
    for i in range(1,N+1):
        if arr[n][i] == 1 and not visited[i]:
            visited[i] = 1
            dfs.append(i)
            DFS(i)
    return

DFS(V)

visited = [0] * (N + 1)
visited[V] = 1
while q:
    n = q.popleft()
    for i in range(1, N+1):
        if arr[n][i] == 1 and not visited[i]:
            bfs.append(i)
            visited[i] = 1
            q.append(i)

print(' '.join(map(str, dfs)))
print(' '.join(map(str, bfs)))