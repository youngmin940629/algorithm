def check_cost(n, a):
    global result
    if n == N:
        if result > a:
            result = a
    elif result < a:
        return
    else:
        for idx in range(N):
            if not visited[idx]:
                a += cost[idx][n]
                visited[idx] = 1
                check_cost(n+1, a)
                visited[idx] = 0
                a -= cost[idx][n]

for tc in range(int(input())):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    result = 99 * N
    check_cost(0, 0)
    print('#{} {}'.format(tc+1, result))