for tc in range(int(input())):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]
    max_fly = 0
    for x in range(N-M+1):
        for y in range(N-M+1):
            tmp_max = 0
            for wid in range(M):
                for hgt in range(M):
                    tmp_max += arr[y+hgt][x+wid]
            if max_fly < tmp_max:
                max_fly = tmp_max
    print('#{}'.format(tc+1), max_fly)