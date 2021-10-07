for tc in range(int(input())):
    V, E = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    course = [[0] * (V + 1) for _ in range(V + 1)]
    result = 0
    visited = [0] * (V + 1)
    distance = [0] * (V + 1)
    for idx in data:
        course[idx[0]][idx[1]] = course[idx[1]][idx[0]] = 1
    def BFS(G, v):
        global visited, distance
        Q = []
        Q.append(v)
        while Q:
            t = Q.pop(0)
            if not visited[t]:
                visited[t] = 1
            for idx in range(1,V+1):
                if G[t][idx] == 1 and visited[idx] == 0:
                    Q.append(idx)
                    visited[idx] = 1
                    distance[idx] = distance[t] + 1
    BFS(course, S)
    if visited[G] == 1:
        print('#{} {}'.format(tc+1, distance[G]))
    else:
        print('#{} {}'.format(tc+1, 0))