from collections import deque

A, B = map(int, input().split())
q = deque()
q.append((A,0))
result = -1
def bfs():
    global result
    while q:
        num, count = q.popleft()
        if num == B:
            result = count
            break
        elif num < B:
            for i in range(2):
                if i == 0:
                    next_num = num * 2
                    if next_num <= B:
                        q.append((next_num, count+1))
                else:
                    next_num = num * 10 + 1
                    if next_num <= B:
                        q.append((next_num, count+1))
bfs()
if result == -1:
    print(result)
else:
    print(result+1)