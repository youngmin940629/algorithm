from collections import deque

def DIJKSTRA(s):
    D = [0xfffff] * (N + 1)
    D[s] = 0
    Q = deque()
    Q.append((s))
    while Q:
        st = Q.popleft()
        for next, w in graph[st]:
            d = D[st] + w
            if d < D[next]:
                D[next] = d
                Q.append((next))
    return D

for tc in range(int(input())):
    N, M, x = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        st, end, w = map(int, input().split())
        graph[st].append((end,w))
    result = 0
    for i in range(1, N+1):
        tmp = 0
        if i != x:
            tmp = DIJKSTRA(i)[x] + DIJKSTRA(x)[i]
            if tmp > result:
                result = tmp
    print('#{} {}'.format(tc+1,result))