for tc in range(10):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]
    cnt = 0
    check_idx = 0
    for x in range(100):
        for y in range(100):
            if data[y][x] == 1:
                break
            else:
                data[y][x] = 0
        for reverse_y in range(99, -1, -1):
            if data[reverse_y][x] == 2:
                break
            else:
                data[reverse_y][x] = 0
        while check_idx < 99:
            if data[check_idx][x] == 1:
                while True:
                    if data[check_idx][x] == 2:
                        cnt += 1
                        break
                    else:
                        check_idx += 1
                    if check_idx > 99:
                        break
            else:
                check_idx += 1
        check_idx = 0
    print('#{} {}'.format(tc+1, cnt))