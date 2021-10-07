for tc in range(10):
    N = int(input())
    data = [list(input().split()) for _ in range(N)]
    L = [0] * (N + 1)
    R = [0] * (N + 1)
    P = [0] * (N + 1)
    def inorder(v):
        if v == 0:return
        inorder(L[v])
        print(data[v-1][1], end = '')
        inorder(R[v])
    for idx in range(len(data)):
        if len(data[idx]) == 3:
            L[int(data[idx][0])] = int(data[idx][2])
        elif len(data[idx]) == 4:
            L[int(data[idx][0])] = int(data[idx][2])
            R[int(data[idx][0])] = int(data[idx][3])
    print('#{} '.format(tc+1), end = '')
    inorder(1)
    print()