import sys
input = sys.stdin.readline

def bellmanFord():
    global result
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for wei, vec in adjList[j]:
                if dist[vec] > wei + dist[j]:
                    dist[vec] = wei + dist[j]
                    if i == N:
                        result = False
                    
T = int(input())
for _ in range(T):
    N, M, W = map(int, input().split())
    INF = 0xffffff
    dist = [INF for _ in range(N + 1)]
    adjList = [[] for _ in range(N + 1)]
    for _ in range(M):
        S, E, T = map(int, input().split())
        adjList[S].append((T, E))
        adjList[E].append((T, S))
    
    for _ in range(W):
        S, E, T = map(int, input().split())
        adjList[S].append((-T, E))
    result = True
    
    bellmanFord()
    print("NO" if result else "YES")