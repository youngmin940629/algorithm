def cook_synergy(n, next_idx):
    global result
    if n == (N // 2):
        a = []
        b = []
        sum_a = sum_b = 0
        for idx in range(N):
            if visited[idx]:
                a.append(idx)
            else:
                b.append(idx)
        for i in range((N // 2) - 1):
            for j in range(i + 1, N // 2):
                sum_a += cook[a[i]][a[j]] + cook[a[j]][a[i]]
                sum_b += cook[b[i]][b[j]] + cook[b[j]][b[i]]
        if abs(sum_a-sum_b) < result:
            result = abs(sum_a-sum_b)
    else:
        for idx in range(next_idx, N):
            if not visited[idx]:
                visited[idx] = 1
                cook_synergy(n+1, idx+1)
                visited[idx] = 0

for tc in range(int(input())):
    N = int(input())
    cook = [list(map(int, input().split())) for _ in range(N)]
    result = 20000
    visited = [0] * N
    cook_synergy(0, 0)
    print('#{} {}'.format(tc+1, result))