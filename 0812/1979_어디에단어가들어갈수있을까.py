for tc in range(int(input())):
    N, K = map(int, input().split())
    square = [list(map(int, input().split())) for i in range(N)]
    cnt = 0
    for x in range(N):
        len_cnt = 0
        for y in range(N):
            if square[y][x] == 0:
                if len_cnt == K:
                    cnt += 1
                len_cnt = 0
            else:
                len_cnt += 1
        if len_cnt == K:
            cnt += 1

    for y in range(N):
        len_cnt = 0
        for x in range(N):
            if square[y][x] == 0:
                if len_cnt == K:
                    cnt += 1
                len_cnt = 0
            else:
                len_cnt += 1
        if len_cnt == K:
            cnt += 1

    print('#{}'.format(tc+1), cnt)