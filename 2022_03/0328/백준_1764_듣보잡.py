import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
listen = []
for _ in range(N):
    listen.append(sys.stdin.readline().rstrip())
see = []
for _ in range(M):
    see.append(sys.stdin.readline().rstrip())

result = list(set(listen) & set(see))
result.sort()
print(len(result))
for i in result:
    print(i)