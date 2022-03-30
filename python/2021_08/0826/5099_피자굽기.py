for tc in range(int(input())):
    N, M = map(int,input().split())
    Ci = list(map(int, input().split()))
    Q = []
    for idx in range(N):
        Q.append([Ci[idx], idx])
    while len(Q) != 1:
        Cheese = Q.pop(0)
        Cheese[0] = Cheese[0] // 2
        if Cheese[0] == 0:
            if N < M:
                Q.append([Ci[N], N])
                N += 1
        else:
            Q.append(Cheese)
    print('#{} {}'.format(tc+1, Q[0][1]+1))