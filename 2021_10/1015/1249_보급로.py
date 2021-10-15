from collections import deque


def bfs():
    global result
    q.append((0,0))
    while q:
        x, y = q.popleft()
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if 0 <= nx < N and 0 <= ny < N:
                if distance[nx][ny] > distance[x][y] + int(arr[nx][ny]):
                    distance[nx][ny] = distance[x][y] + int(arr[nx][ny])
                    q.append((nx,ny))


for tc in range(int(input())):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    q = deque()
    distance = [[0xfffff] * N for _ in range(N)]
    distance[0][0] = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    bfs()
    print('#{} {}'.format(tc+1, distance[N-1][N-1]))