def bubble(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

for tc in range(int(input())):
    N, M = map(int, input().split())
    weight = list(map(int, input().split()))
    load = list(map(int, input().split()))
    result = 0
    visited = [0] * N
    bubble(weight)
    bubble(load)
    for i in range(M):
        for j in range(N):
            if load[i] >= weight[j] and visited[j] == 0:
                result += weight[j]
                visited[j] = 1
                break
    print('#{} {}'.format(tc+1, result))
    print(f'#{tc + 1} {result}')