from collections import deque
def bfs():
    while q:
        x, y = q.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < N and 0 <= ny < N:
                cost = 1
                if data[nx][ny] > data[x][y]:
                    cost = cost + (data[nx][ny] - data[x][y])
                if distance[nx][ny] > (distance[x][y] + cost):
                    distance[nx][ny] = (distance[x][y] + cost)
                    q.append((nx,ny))
for tc in range(int(input())):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    distance = [[0xffffff] * N for _ in range(N)]
    distance[0][0] = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque()
    q.append((0,0))
    bfs()
    print('#{} {}'.format(tc+1, distance[N-1][N-1]))