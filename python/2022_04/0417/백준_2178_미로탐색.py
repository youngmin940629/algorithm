from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
q = deque()
q.append((0,0))
min = N * M
while q:
    x,y = q.popleft()
    if x == N-1 and y == M-1:
        break
    for dir in range(4):
        nx,ny = x+dx[dir] , y+dy[dir]
        if 0<=nx<N and 0<=ny<M and arr[nx][ny] == 1:
            arr[nx][ny] = arr[x][y] + 1
            q.append((nx,ny))
print(arr[N-1][M-1])