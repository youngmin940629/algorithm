for tc in range(int(input())):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    sum_check = 0
    for i in range(1<<N):
        for j in range(N+1):
            if i & (1<<j):
                sum_check += arr[j]
        if sum_check == K:
            cnt += 1
        sum_check = 0
    print('#{}'.format(tc + 1), cnt)