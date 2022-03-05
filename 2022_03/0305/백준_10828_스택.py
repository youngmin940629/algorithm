import sys

N = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(N):
    x = sys.stdin.readline().rstrip()
    if x == 'pop':
        if arr:
            print(arr.pop())
        else:
            print(-1)
    elif x == 'size':
        print(len(arr))
    elif x == 'empty':
        if arr:
            print(0)
        else:
            print(1)
    elif x == 'top':
        if arr:
            print(arr[-1])
        else:
            print(-1)
    else:
        arr.append(x.split()[-1])
