for tc in range(int(input())):
    N = int(input())
    color = [list(map(int, input().split())) for i in range(N)]
    square = [[0] * 10 for height in range(10)]
    result = 0
    for cnt in range(N):
        if color[cnt][4] == 1:
            for x in range(color[cnt][0], color[cnt][2] + 1):
                for y in range(color[cnt][1], color[cnt][3] + 1):
                    square[y][x] = 1
    for cnt in range(N):
        if color[cnt][4] == 2:
            for x in range(color[cnt][0], color[cnt][2] + 1):
                for y in range(color[cnt][1], color[cnt][3] + 1):
                    if square[y][x] == 1:
                        result += 1
    print('#{}'.format(tc+1), result)