for tc in range(10):
    T = int(input())
    data = list(map(int, input().split()))
    f, r = 0, 0
    s = [0] * 9
    def isEmpty():
        return f == r
    def isFull():
        return (r + 1) % 9 == f
    def enQueue(item):
        global r
        if isFull():
            return
        else:
            r = (r + 1) % 9
            s[r] = item
    def deQueue():
        global f
        if isEmpty():
            return
        else:
            f = (f + 1) % 9
            return s[f]
    for val in data:
        enQueue(val)
    while True:
        for cycle in range(1, 6):
            tmp = deQueue() - cycle
            if tmp > 0:
                enQueue(tmp)
            else:
                enQueue(0)
                break
        if tmp <= 0:
            break
    print('#{}'.format(tc+1), end = ' ')
    for _ in range(8):
        print(deQueue(), end = ' ')
    print()