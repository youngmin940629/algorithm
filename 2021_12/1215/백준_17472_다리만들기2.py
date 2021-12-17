from collections import deque

def bfs():
    global island_num
    while q:
        x, y = q.popleft()
        arr[x][y] = island_num
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] and (nx,ny) not in visited:
                    q.append((nx,ny))
                    visited.append((nx,ny))
    island_num += 1

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
island_num = 1
q = deque()
edge = []
visited = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for x in range(N):
    for y in range(M):
        if arr[x][y] and (x,y) not in visited:
            q.append((x,y))
            visited.append((x,y))
            bfs()
print(arr)