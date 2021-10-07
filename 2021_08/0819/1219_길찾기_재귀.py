for tc in range(10):
    t, N = map(int, input().split())
    G = [[0] * 100 for _ in range(100)]
    data = list(map(int, input().split()))
    for idx in range(N):
        G[data[idx * 2]][data[idx * 2 + 1]] = 1
    visited = [0] * 100
    def dfs(v):
        visited[v] = 1
        for i in range(100):
            if G[v][i] == 1 and not visited[i]:
                dfs(i)
    dfs(0)
    if visited[99] == 1:
        print('#{} {}'.format(t, 1))
    else:
        print('#{} {}'.format(t, 0))