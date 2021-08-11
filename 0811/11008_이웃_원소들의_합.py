for tc in range(1, int(input()) + 1):
    size = int(input())
    arr = [list(map(int, input().split())) for i in range(size)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    total = 0
    rx, ry = 0, 0
    for x in range(size):
        for y in range(size):
            total_tmp = 0
            for i in range(4):
                testX = x + dx[i]
                testY = y + dy[i]
                if 0 <= testY < size and 0 <= testX < size:
                    total_tmp += arr[testX][testY]
                    if total < total_tmp:
                        total = total_tmp
                        rx, ry = x, y
                    elif total == total_tmp:
                        if rx > x:
                            rx = x
                        else:
                            if ry > y:
                                ry = y
    print(f'#{tc}', rx, ry, total)