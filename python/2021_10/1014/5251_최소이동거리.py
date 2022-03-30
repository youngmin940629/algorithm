for tc in range(int(input())):
    N, E = map(int, input().split())
    G = [[] for _ in range(N+1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        G[u].append((v, w))
    D = [0xffffff] * (N+1)
    Q = [0]
    D[0] = 0
    while Q:
        u = Q.pop(0)
        for v, w in G[u]:
            if D[v] > D[u] + w:
                D[v] = D[u] + w
                Q.append(v)
    print('#{} {}'.format(tc+1, D[N]))