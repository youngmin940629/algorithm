def issafe(a, b):
    if 0 <= a < N and 0 <= b < N:
        return True
    else:
        False
for tc in range(int(input())):
    N = int(input())
    miro = [list(map(str, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    distance = [[0]*N for _ in range(N)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    Q = []
    result = 0
    for i in range(N):
        for j in range(N):
            if miro[j][i] == '2':
                Q.append([i,j])
                visited[j][i] = 1
                break
    while Q:
        coordinate = Q.pop(0)
        x, y = coordinate[0], coordinate[1]
        for dir in range(4):
            if issafe(x+dx[dir],y+dy[dir]):
                if visited[y+dy[dir]][x+dx[dir]] == 0 and miro[y+dy[dir]][x+dx[dir]] == '0':
                    Q.append([x+dx[dir], y+dy[dir]])
                    visited[y+dy[dir]][x+dx[dir]] = 1
                    distance[y+dy[dir]][x+dx[dir]] = distance[y][x] + 1
                elif visited[y+dy[dir]][x+dx[dir]] == 0 and miro[y+dy[dir]][x+dx[dir]] == '3':
                    result = distance[y][x]
    print('#{} {}'.format(tc+1, result))