def is_safe(x, y):
    return 0 <= x < N and 0 <= y < N

def min_sum(x, y, s):
    global result
    if s > result:
        return
    if x == (N - 1) and y == (N - 1):
        if result > s:
            result = s
            return
    else:
        for dir in range(2):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if is_safe(nx, ny):
                s += data[nx][ny]
                min_sum(nx, ny, s)
                s -= data[nx][ny]

for tc in range(int(input())):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    dx = [1, 0]
    dy = [0, 1]
    result = 0
    for y in range(N):
        for x in range(N):
            result += data[y][x]
    min_sum(0, 0, data[0][0])
    print('#{} {}'.format(tc+1, result))
    print(f'#{tc+1} {result}')