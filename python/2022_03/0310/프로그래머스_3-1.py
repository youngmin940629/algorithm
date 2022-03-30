
def solution(m, n, puddles):
    answer = 0
    arr = list([0] * (m+1) for _ in range(n+1))
    for x in range(1,n+1):
        for y in range(1,m+1):
            if x == 1 and y == 1:
                arr[x][y] = 1
            elif [y,x] not in puddles:
                arr[x][y] = arr[x-1][y] + arr[x][y-1]
    answer = arr[n][m] % 1000000007
    return answer

solution(4,3,[[2,2]])