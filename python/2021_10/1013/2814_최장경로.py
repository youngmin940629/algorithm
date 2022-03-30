from collections import deque

def dfs(node, cnt):
    global result
    if result < cnt:
        result = cnt
    for idx in range(N+1):
        if graph[node][idx]:
            if not visited[idx]:
                visited[idx] = 1
                dfs(idx, cnt+1)
                visited[idx] = 0

for tc in range(int(input())):
    N, M = map(int, input().split())
    graph =[[0] * (N+1) for _ in range(N+1)]
    visited = [0] * (N+1)
    result = 0
    for _ in range(M):
        x, y = map(int, input().split())
        graph[x][y] = graph[y][x] = 1
    q = deque()
    for i in range(1, N+1):
        visited[i] = 1
        dfs(i, 1)
        visited[i] = 0
    print('#{} {}'.format(tc+1, result))