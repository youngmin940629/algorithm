for tc in range(int(input())):
    N = int(input())
    count_arr = [0] * 200
    max = 0
    for _ in range(N):
        start, end = map(int, input().split())
        if start > end:
            start, end = end, start
        for route in range(((start-1)//2), ((end-1)//2)+1):
            count_arr[route] += 1
    for result in count_arr:
        if max < result:
            max = result
    print('#{} {}' .format(tc+1, max))