def heap_push(n):
    global heap_size
    heap_size += 1
    heap[heap_size] = n
    c = heap_size
    p = c // 2
    while p and heap[p] > heap[c]:
        if heap[p] > heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
        p, c = p//2, p



for tc in range(int(input())):
    N = int(input())
    data = list(map(int, input().split()))
    heap = [0] * (N+1)
    heap_size = 0
    result = 0
    for num in data:
        heap_push(num)
    while N:
        N = N // 2
        result += heap[N]
    print('#{} {}'.format(tc+1, result))