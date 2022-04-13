import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split())) 
arr = [0] + arr
for i in range(1, N+1):
    arr[i] = arr[i] + arr[i-1]
for _ in range(M):
    st, end = map(int, input().split())
    print(arr[end] - arr[st-1])