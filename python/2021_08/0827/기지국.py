for tc in range(int(input())):
    N = int(input())
    data = [list(input()) for _ in range(N)]
    cnt = [[0] * N for _ in range(N)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for y in range(N):
        for x in range(N):
            if data[y][x] == 'H':
                cnt[y][x] = 1
            elif data[y][x] == 'A':
                cnt[y][x] = 2
            elif data[y][x] == 'B':
                cnt[y][x] = 3
            elif data[y][x] == 'C':
                cnt[y][x] = 4
    for y in range(N):
        for x in range(N):
            if cnt[y][x] == 2:
                for dir in range(4):
                    next_x = x + dx[dir]
                    next_y = y + dy[dir]
                    if 0 <= next_x < N and 0 <= next_y < N and cnt[next_y][next_x] == 1:
                        cnt[next_y][next_x] = 0
            elif cnt[y][x] == 3:
                for i in range(1,3):
                    for dir in range(4):
                        next_x = x + dx[dir] * i
                        next_y = y + dy[dir] * i
                        if 0 <= next_x < N and 0 <= next_y < N and cnt[next_y][next_x] == 1:
                            cnt[next_y][next_x] = 0
            elif cnt[y][x] == 4:
                for i in range(1,4):
                    for dir in range(4):
                        next_x = x + dx[dir] * i
                        next_y = y + dy[dir] * i
                        if 0 <= next_x < N and 0 <= next_y < N and cnt[next_y][next_x] == 1:
                            cnt[next_y][next_x] = 0
    result = 0
    for y in range(N):
        for x in range(N):
            if cnt[y][x] == 1:
                result += 1
    print('#{} {}'.format(tc+1, result))