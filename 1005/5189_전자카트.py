def cart(y, s):
    global result
    if result < s:
        return
    if y == 0:
        result = s
        return
    else:
        if 1 not in visited:
            s += data[y][0]
            cart(0, s)
        else:
            for idx in range(1, N):
                if visited[idx] == 1:
                    s += data[y][idx]
                    visited[idx] = 0
                    cart(idx, s)
                    s -= data[y][idx]
                    visited[idx] = 1


for tc in range(int(input())):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] + [1] * (N - 1)
    result = 0
    for x in range(N):
        for y in range(N):
            result += data[x][y]
    for y in range(1, N):
        visited[y] = 0
        cart(y, data[0][y])
        visited[y] = 1
    print('#{} {}'.format(tc+1, result))
    print(f'#{tc + 1} {result}')