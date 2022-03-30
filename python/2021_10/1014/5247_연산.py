from collections import deque

def bfs(N,M):
    global result
    q.append((N,0))
    visited = [0] * (1000001)
    while q:
        num, cnt = q.popleft()
        if num == M:
            return cnt
        if 0 < num + 1 <= 1000000 and not visited[num+1]:
            q.append((num+1, cnt+1))
            visited[num+1] = cnt+1
        if 0 < num - 1 <= 1000000 and not visited[num-1]:
            q.append((num-1, cnt+1))
            visited[num - 1] = cnt+1
        if 0 < num * 2 <= 1000000 and not visited[num*2]:
            q.append((num*2, cnt+1))
            visited[num * 1] = cnt+1
        if 0 < num - 10 <= 1000000 and not visited[num-10]:
            q.append((num-10, cnt+1))
            visited[num - 10] = cnt+1


for tc in range(int(input())):
    N, M = map(int, input().split())
    q = deque()
    print('#{} {}'.format(tc+1, bfs(N,M)))