for tc in range(1, int(input())+1):
    max_value = 0
    min_value = 1000000
    M, N = map(int, input('').split())
    arr = list(map(int, input().split()))
    for cnt in range(0, M - N + 1):
        total = 0
        for idx in range(0, N):
            total += arr[cnt + idx]
        if max_value < total: max_value = total
        if min_value > total: min_value = total
    print('#{}'.format(tc), max_value - min_value)