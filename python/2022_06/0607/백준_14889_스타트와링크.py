N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0xffffff
visit = [0] * N
def dfs(n, idx):
    global result
    if n == N // 2:
        a = b = 0
        for i in range(N):
            for j in range(i+1, N):
                if visit[i] and visit[j]:
                    a += (arr[i][j] + arr[j][i])
                if not visit[i] and not visit[j]:
                    b += (arr[i][j] + arr[j][i])
        result = min(result, abs(a-b))
    else:
        for k in range(idx, N):
            if not visit[k]:
                visit[k] = 1
                dfs(n+1, k+1)
                visit[k] = 0
dfs(0,0)
print(result)