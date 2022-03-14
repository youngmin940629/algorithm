import sys

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(sys.stdin.readline().split())
arr.sort()
for num in arr:
    print(num[0])