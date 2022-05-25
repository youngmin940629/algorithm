import sys
import heapq
input = sys.stdin.readline

N = int(input())
heapq1 = []
heapq2 = []
result = []
for i in range(N):
    num = int(input())
    if len(heapq1) == len(heapq2):
        heapq.heappush(heapq1, (-num, num))
    else:
        heapq.heappush(heapq2, num)
    
    if heapq2 and heapq1[0][1] > heapq2[0]:
        tmp_min = heapq.heappop(heapq2)
        tmp_max = heapq.heappop(heapq1)[1]
        heapq.heappush(heapq1, (-tmp_min, tmp_min))
        heapq.heappush(heapq2, tmp_max)
    result.append(heapq1[0][1])

for i in result:
    print(i)