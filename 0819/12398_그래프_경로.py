for tc in range(int(input())):
    V, E = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    course = [[0]*(V+1) for _ in range(V+1)]
    result = 0
    visited = [0] * (V+1)
    stack = [S]
    for idx in data:
        course[idx[0]][idx[1]] = 1
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = 1
            for i in range(1, V+1):
                if not visited[i] and course[v][i]:
                    stack.append(i)
    if visited[G] == 1:
        result = 1
    print('#{} {}'.format(tc+1, result))


