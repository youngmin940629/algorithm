for tc in range(int(input())):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    result = [[0] * 3 for _ in range(N)]
    for case in range(3):
        if case == 0:
            tmp_result = 0
            for i in range(N): #90
                for j in range(N):
                    tmp_result += data[j][i] * (10**j)
                result[i][0] = tmp_result
                tmp_result = 0
        elif case == 1:
            tmp_result = 0
            for i in range(N-1, -1, -1): #180
                for j in range(N):
                    tmp_result += data[i][j] * (10 ** j)
                result[N-1-i][1] = tmp_result
                tmp_result = 0
        elif case == 2:
            tmp_result = 0
            for i in range(N - 1, -1, -1):  # 270
                for j in range(N):
                    tmp_result += data[j][i] * (10 ** (N-1-j))
                result[N - 1 - i][2] = tmp_result
                tmp_result = 0
    print('#{}'.format(tc+1))
    for i in range(N):
        print(' '.join(map(str, result[i])))