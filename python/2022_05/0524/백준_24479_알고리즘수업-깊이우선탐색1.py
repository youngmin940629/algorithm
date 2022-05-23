import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N, M, R = map(int, input().split())
arr = [[] for _ in range(M+1)]
for _ in range(N):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)
for i in range(1, len(arr)):
    arr[i].sort()
visit = [0] * (M+1)
visit[R] = 1
def dfs(n):
    for next in arr[n]:
        if not visit[next]:
            visit[next] = visit[n] + 1
            dfs(next)
dfs(R)
for i in range(1,M+1):
    print(visit[i])