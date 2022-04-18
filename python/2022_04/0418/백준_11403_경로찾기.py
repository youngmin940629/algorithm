from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
q = deque()

def bfs():
    global N
    visited = [0] * N
    while q:
        idx = q.popleft()
        for index, value in enumerate(arr[idx]):
            if not visited[index] and value == 1:
                visited[index] = 1
                q.append(index)
    return visited

for a in range(N):
    q.append(a)
    print(' '.join(map(str, bfs())))