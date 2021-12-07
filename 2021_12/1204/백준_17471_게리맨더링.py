N = int(input())
people = list(map(int, input().split()))
arr = [[0] * (N+1) for _ in range(N+1)]
for i in range(1,N+1):
    data = list(map(int, input().split()))
    for j in range(1, len(data)):
        arr[i][data[j]] = arr[data[j]][i] = 1
