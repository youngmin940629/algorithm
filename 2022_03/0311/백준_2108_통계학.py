import sys
from collections import Counter

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))
print(round(sum(arr)/N))
arr.sort()
print(arr[N//2])
cnt_li = Counter(arr).most_common()
if len(cnt_li) > 1 and cnt_li[0][1]==cnt_li[1][1]:
    print(cnt_li[1][0])
else:
    print(cnt_li[0][0])

print(arr[N-1]-arr[0])