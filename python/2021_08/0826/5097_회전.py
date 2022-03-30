for tc in range(int(input())):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    Q = [0] * (len(arr) + 1)
    f = r = 0
    def isFull():
        return (r + 1) % (len(arr) + 1) == f
    def isEmpty():
        return f == r
    def enQueue(item):
        global r
        if isFull():return
        else:
            r = (r + 1) % (len(arr) + 1)
            Q[r] = item
    def deQueue():
        global f
        if isEmpty():return
        else:
            f = (f + 1) % (len(arr) + 1)
            return Q[f]
    for idx in range(len(arr)):
        enQueue(arr[idx])
    for i in range(M):
        enQueue(deQueue())
    print('#{} {}'.format(tc+1, Q[((f + 1) % (len(arr) + 1))]))