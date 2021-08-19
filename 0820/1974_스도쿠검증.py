for tc in range(int(input())):
    square = []
    for _ in range(9):
        square.append(list(map(int, input().split())))
    check_arr = [1] * 3
    result = 1
    for x in range(9):
        cnt_arr = [0] * 9
        for y in range(9):
            cnt_arr[square[y][x]-1] += 1
        for check in cnt_arr:
            if check != 1:
                check_arr[0] = 0
                break
        if check_arr[0] == 0:
            break
    for y in range(9):
        cnt_arr = [0] * 9
        for x in range(9):
            cnt_arr[square[y][x]-1] += 1
        for check in cnt_arr:
            if check != 1:
                check_arr[1] = 0
                break
        if check_arr[1] == 0:
            break
    for y in range(3):
        for x in range(3):
            cnt_arr = [0] * 9
            for i in range(3):
                for j in range(3):
                    cnt_arr[square[y*3+i][x*3+j]-1] += 1
            for check in cnt_arr:
                if check != 1:
                    check_arr[2] = 0
                    break
            if check_arr[2] == 0:
                break
    for rst in check_arr:
        if rst == 0:
            result = 0
    print('#{} {}'.format(tc+1, result))