for tc in range(int(input())):
    N = int(input())
    omok = [list(input()) for _ in range(N)]
    dx = [1, 1, 0, -1, -1, -1, 0, 1]  # 0부터 오른쪽 시계방향
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    result = 'NO'
    def omok_check(K, x, y, dir):
        global result
        if K == 5:
            result = 'YES'
            return
        elif 0 <= x < N and 0 <= y < N:
            if omok[y][x] == '.':
                return
            else:
                if 0 <= x+dx[dir] < N and 0 <= y+dy[dir] < N:
                    if omok[y+dy[dir]][x+dx[dir]] == 'o':
                        omok_check(K+1, x+dx[dir], y+dy[dir], dir)
        else:
            return
    for y in range(N):
        for x in range(N):
            if omok[y][x] == 'o':
                for i in range(8):
                    if 0 <= x + dx[i] < N and 0 <= y + dy[i] < N:
                        if omok[y + dy[i]][x + dx[i]] == 'o':
                            omok_check(1, x, y, i)
    print('#{} {}'.format(tc+1, result))