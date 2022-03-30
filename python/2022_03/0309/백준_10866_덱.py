from collections import deque
import sys

N = int(sys.stdin.readline())
arr = deque()
for _ in range(N):
    order = sys.stdin.readline().split()
    if order[0] == 'pop_front':
        if arr:
            print(arr.popleft())
        else:
            print(-1)
    elif order[0] == 'pop_back':
        if arr:
            print(arr.pop())
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(arr))
    elif order[0] == 'empty':
        if arr:
            print(0)
        else:
            print(1)
    elif order[0] == 'front':
        if arr:
            print(arr[0])
        else:
            print(-1)
    elif order[0] == 'back':
        if arr:
            print(arr[-1])
        else:
            print(-1)
    elif order[0] == 'push_front':
        arr.appendleft(order[1])
    elif order[0] == 'push_back':
        arr.append(order[1])