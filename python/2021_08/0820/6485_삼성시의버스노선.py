for tc in range(int(input())):
    N = int(input())
    data1 = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    data2 = []
    result = [0]*P
    for _ in range(P):
        data2 = data2 + [int(input())]
    for station in range(P):
        for i in range(N):
            if data1[i][0] <= data2[station] <= data1[i][1]:
                result[station] += 1
    print('#{}'.format(tc+1), ' '.join(map(str,result)))