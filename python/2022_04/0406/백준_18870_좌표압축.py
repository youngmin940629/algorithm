import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

tmp = list(set(arr))
tmp.sort()

dic = {tmp[i] : i for i in range(len(tmp))}
for i in arr:
    print(dic[i], end = ' ')