def chess(st_x,st_y):
    count = 64
    for case in range(2):
        tmp = 0
        for i in range(st_x, st_x+8):
            for j in range(st_y, st_y+8):
                if case == 0:
                    if (i - st_x) % 2 == 0:
                        if (j - st_y) % 2 == 0 and arr[i][j] == 'B':
                            tmp += 1
                        elif (j - st_y) % 2 == 1 and arr[i][j] == 'W':
                            tmp += 1
                    else:
                        if (j - st_y) % 2 == 0 and arr[i][j] == 'W':
                            tmp += 1
                        elif (j - st_y) % 2 == 1 and arr[i][j] == 'B':
                            tmp += 1
                else:
                    if (i - st_x) % 2 == 0:
                        if (j - st_y) % 2 == 0 and arr[i][j] == 'W':
                            tmp += 1
                        elif (j - st_y) % 2 == 1 and arr[i][j] == 'B':
                            tmp += 1
                    else:
                        if (j - st_y) % 2 == 0 and arr[i][j] == 'B':
                            tmp += 1
                        elif (j - st_y) % 2 == 1 and arr[i][j] == 'W':
                            tmp += 1
        count = min(count, tmp)
    return count

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(input()))
result = 64
for x in range(N-7):
    for y in range(M-7):
        result = min(result, chess(x,y))
print(result)