for tc in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 500
    visited = [0]*N
    def min_sum(a, cur_sum):
        global result
        if cur_sum > result:
            return
        if a == N:
            result = cur_sum
        else:
            for i in range(N):
                if visited[i] == 0:
                    visited[i] = 1
                    cur_sum += arr[a][i]
                    min_sum(a+1, cur_sum)
                    visited[i] = 0
                    cur_sum -= arr[a][i]
    min_sum(0, 0)
    print('#{} {}'.format(tc+1, result))