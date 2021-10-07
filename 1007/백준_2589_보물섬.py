from collections import deque

def bfs(x, y):
    q.append((x,y,0))
    visited = [[0] * height for _ in range(width)]
    visited[x][y] = 1
    distance = 0
    while q:
        x, y, d = q.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= ny < height and 0 <= nx < width:
                if not visited[nx][ny] and map[nx][ny] == 'L':
                    q.append((nx, ny, d+1))
                    visited[nx][ny] = visited[x][y] + 1
                    distance = max(d, visited[nx][ny])
    return distance - 1

width, height = map(int, input().split())
map = [list(input()) for _ in range(width)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result = 0
q = deque()
for y in range(height):
    for x in range(width):
        if map[x][y] == 'L':
            result = max(bfs(x,y), result)
print(result)