def power(n, a):
    global result
    if result >= a:
        return
    if n == N:
        result = a
    for idx in range(N):
        if not visited[idx]:
            visited[idx] = 1
            power(n+1, a * work[idx][n] / 100)
            visited[idx] = 0


for tc in range(int(input())):
    N = int(input())
    work = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    result = 0
    power(0, 100)
    print('#{} {:.6f}'.format(tc+1, result))