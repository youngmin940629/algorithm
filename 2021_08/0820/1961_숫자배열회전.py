for tc in range(int(input())):
    N = int(input())
    data = [list(input().split()) for _ in range(N)]
    result1 = [[] for _ in range(N)]
    result2 = [[] for _ in range(N)]
    result3 = [[] for _ in range(N)]
    for case in range(3):
        if case == 0:
            tmp_result = 0
            for i in range(N): #90
                for j in range(N):
                    result1[i].append(data[N-1-j][i])
        elif case == 1:
            tmp_result = 0
            for i in range(N): #180
                for j in range(N):
                    result2[i].append(data[N-1-i][N-1-j])
        elif case == 2:
            tmp_result = 0
            for i in range(N):  # 270
                for j in range(N):
                    result3[i].append(data[j][N-1-i])
    print('#{}'.format(tc+1))
    for idx in range(N):
        print('{} {} {}'.format(''.join(map(str, result1[idx])), ''.join(map(str, result2[idx])), ''.join(map(str, result3[idx]))))