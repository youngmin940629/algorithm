from collections import deque

def bfs():
    while que:
        x, y = que.popleft()
        for dir in range(4):
            next_x = x + dx[dir]
            next_y = y + dy[dir]
            if 0 <= next_x < M and 0 <= next_y < N:
                if visited[next_y][next_x] == -1:
                    que.append((next_x, next_y))
                    visited[next_y][next_x] = visited[y][x] + 1


for tc in range(int(input())):
    N, M = map(int,input().split())
    road = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    que = deque()
    for _ in range(N):
        road.append(list(input()))
    visited = [[-1] * M for _ in range(N)]
    for y in range(N):
        for x in range(M):
            if road[y][x] == 'W':
                visited[y][x] = 0
                que.append((x, y))
    cnt = 0
    bfs()
    for y in range(N):
        for x in range(M):
            cnt += visited[y][x]
    print('#{} {}'.format(tc+1, cnt))