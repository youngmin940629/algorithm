for i in range(10):
    tc, N = map(int, input().split())
    data = list(map(int, input().split()))
    course = [[0]*(100) for _ in range(100)]
    result = 0
    visited = [0] * (100)
    stack = [0]
    for idx in range(N):
        course[data[idx*2]][data[idx*2 + 1]] = 1
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = 1
            for i in range(100):
                if not visited[i] and course[v][i]:
                    stack.append(i)
    if visited[99] == 1:
        result = 1
    print('#{} {}'.format(tc, result))