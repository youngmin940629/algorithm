from collections import deque

def bfs(st,end):
    visited = [[0] * N for _ in range(N)]
    cnt = 1
    global max_check, check_idx
    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if room[nx][ny] - room[x][y] == 1:
                    q.append((nx,ny))
                    cnt += 1
    if max_check < cnt:
        max_check = cnt
        check_idx = room[st][end]
    elif max_check == cnt:
        if check_idx > room[st][end]:
            check_idx = room[st][end]


for tc in range(int(input())):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    max_check = 0
    check_idx = 10 ** 3
    q = deque()
    for x in range(N):
        for y in range(N):
            q.append((x,y))
            bfs(x,y)
    print('#{} {} {}'.format(tc+1, check_idx, max_check))