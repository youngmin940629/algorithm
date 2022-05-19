from collections import deque

N, M = map(int, input().split())
arr = list(map(int, input().split()))
q = deque([i for i in range(1, N+1)])

result = 0
for num in arr:
    while True:
        if q[0] == num:
            q.popleft()
            break
        else:
            if q.index(num) < len(q) / 2:
                q.append(q.popleft())
                result += 1
            else:
                while q[0] != num:
                    q.appendleft(q.pop())
                    result += 1
print(result)