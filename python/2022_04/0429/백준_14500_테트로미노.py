N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result = 0
max_val = 0
for i in range(N):
    for j in range(M):
        if max_val < arr[i][j]:
            max_val = arr[i][j]

def dfs(x,y,i,total):
    global result
    if result >= total + max_val * (3-i):
        return
    if i == 3:
        result = max(result, total)
        return
    else:
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                if i == 1:
                    visited[nx][ny] = 1
                    dfs(x, y, i+1, total + arr[nx][ny])
                    visited[nx][ny] = 0
                visited[nx][ny] = 1
                dfs(nx, ny, i + 1, total + arr[nx][ny])
                visited[nx][ny] = 0

for x in range(N):
    for y in range(M):
        visited[x][y] = 1
        dfs(x, y, 0, arr[x][y])
        visited[x][y] = 0
print(result)