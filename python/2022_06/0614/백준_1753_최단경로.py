import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
arr = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    arr[u].append([v,w])

dp = [0xffffff] * (V+1)
heap = []

def dijkstra(st):
    dp[st] = 0
    heapq.heappush(heap, (0,st))
    while heap:
        value, node = heapq.heappop(heap)
        if dp[node] < value:
            continue

        for next, v in arr[node]:
            next_value = v + value
            if next_value < dp[next]:
                dp[next] = next_value
                heapq.heappush(heap, (next_value, next))

dijkstra(K)
for i in range(1, len(dp)):
    if dp[i] == 0xffffff:
        print("INF")
    else:
        print(dp[i])