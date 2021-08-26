for tc in range(int(input())):
    N = int(input())
    data = [i for i in range(1,N+1)]
    Q = [0] * 2 * N
    f = r = -1
    def isFull():
        return r == len(Q) - 1
    def isEmpty():
        return f == r
    def enQueue(item):
        global r
        if isFull():
            return
        else:
            r = r + 1
            Q[r] = item
    def deQueue():
        global f
        if isEmpty():
            return
        else:
            f = f + 1
            return Q[f]
    for idx in range(len(data)):
        enQueue(data[idx])
    for cnt in range(len(data)-1):
        deQueue()
        result = deQueue()
        enQueue(result)
    print('#{} {}'.format(tc+1, result))