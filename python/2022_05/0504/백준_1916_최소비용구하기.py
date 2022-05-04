from heapq import heappop, heappush
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())
bus = [[] for _ in range(N+1)]
for _ in range(M):
    st, end, cost = map(int, input().split())
    bus[st].append((end,cost))
dp = [0xffffff] * (N+1)
dp[1] = 0
start, end = map(int, input().split())
q = deque()
q.append((start,0))
while q:
    city, cost = q.popleft()
    for next in bus[city]:
        next_city, next_cost = next[0], next[1]
        if (cost + next_cost) < dp[next_city]:
            dp[next_city] = cost + next_cost
            q.append((next_city,dp[next_city]))
print(dp[end])

def dijkstra(s):
    dp[s] = 0
    heap = []
    heappush(heap, [0,s])
    while heap:
        w,n = heappop(heap)
        if dp[n] < w:
            continue
        for next, cost in bus[n]:
            if dp[next] > cost+w:
                dp[next] = cost+w
                heappush(heap,[dp[next],next])
dijkstra(start)
print(dp[end])