from collections import deque

def bfs():
    global cnt
    visit = [[0] * 5 for _ in range(5)]
    while q:
        x,y,som,num = q.popleft()
        if num == 7:
            if som >= 4:
                cnt += 1
        else:
            for dir in range(4):
                nx = x + dx[dir]
                ny = y + dy[dir]
                if 0 <= nx < 5 and 0 <= ny < 5 and not visit[nx][ny]:
                    visit[nx][ny] = 1
                    if students[nx][ny] == 'S':
                        q.append((nx,ny,som+1,num+1))
                    elif students[nx][ny] == 'Y':
                        q.append((nx,ny,som,num+1))

students = [list(input()) for _ in range(5)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
q = deque()
cnt = 0
for x in range(5):
    for y in range(5):
        q.append((x,y,0,0))
print(cnt)