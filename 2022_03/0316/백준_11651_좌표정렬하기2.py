import sys
N = int(sys.stdin.readline())
destination = []
for _ in range(N):
    destination.append(list(map(int, sys.stdin.readline().split())))
destination.sort(key = lambda x : (x[1], x[0]))
for i in range(N):
    print(' '.join(map(str, destination[i])))