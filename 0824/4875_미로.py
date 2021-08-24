for tc in range(int(input())):
    N = int(input())
    miro = [list(map(str, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    stack = []
    result = 0
    def find(x, y):
        global result
        if x+1 < N:
            if miro[y][x+1] == '0' and visited[y][x+1] == 0:
                visited[y][x+1] = 1
                find(x+1, y)
            elif miro[y][x+1] == '3':
                result = 1
        if 0 <= x-1:
            if miro[y][x-1] == '0' and visited[y][x-1] == 0:
                visited[y][x-1] = 1
                find(x-1, y)
            elif miro[y][x-1] == '3':
                result = 1
        if y+1 < N:
            if miro[y+1][x] == '0' and visited[y+1][x] == 0:
                visited[y+1][x] = 1
                find(x, y+1)
            elif miro[y+1][x] == '3':
                result = 1
        if 0 <= y-1:
            if miro[y-1][x] == '0' and visited[y-1][x] == 0:
                visited[y-1][x] = 1
                find(x, y-1)
            elif miro[y-1][x] == '3':
                result = 1
    for i in range(N):
        for j in range(N):
            if miro[j][i] == '2':
                st_a, st_b = i, j
                visited[i][j] = 1
                break
    find(st_a,st_b)
    print("#{} {}".format(tc+1, result))