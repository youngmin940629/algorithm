from collections import deque

N = int(input())
friend =[[0] * (N+1) for _ in range(N+1)]
while True:
    a, b = map(int, input().split())
    if a != -1 and b != -1:
        friend[a][b] = friend[b][a] = 1
    else:
        break
score = [0] * (N+1)
for person in range(1, N+1):
    visited = [[0] * (N + 1) for _ in range(N + 1)]
    q = deque()
    tmp = 0
    for next in range(1, N+1):
        if friend[person][next] == 1:
            visited[person][next] = visited[next][person] = 1
            q.append((person, next))
    while q:
        st, end = q.popleft()
        for next_friend in range(1, N+1):
            if friend[end][next_friend] == 1 and not visited[end][next_friend]:
                visited[end][next_friend] = visited[next_friend][end] = visited[st][end] + 1
                q.append((end, next_friend))
    for x in range(1,N+1):
        for y in range(1,N+1):
            if visited[x][y] > tmp:
                tmp = visited[x][y]
    score[person] = tmp

min_score = min(score[1:])
result = []
num = 0
for idx in range(1, N+1):
    if min_score == score[idx]:
        result.append(idx)
        num += 1
print(min_score, num)
print(' '.join(map(str, result)))