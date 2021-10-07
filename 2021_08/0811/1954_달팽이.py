for tc in range(1, int(input())+1):
    N = int(input())
    snail = [[0] * N for i in range(N)]
    num = 1
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    i = 0
    x, y = 0, -1
    cnt = 0
    while cnt < N**2:
        if 0 <= x+dx[i] < N and 0 <= y+dy[i] < N and snail[x+dx[i]][y+dy[i]] == 0:
            x = x+dx[i]
            y = y+dy[i]
            snail[x][y] = cnt + 1
            cnt += 1
        else:
            i = (i + 1) % 4
    print('#{}'.format(tc))
    for idx in range(N):
        print(' '.join(map(str, snail[idx])))