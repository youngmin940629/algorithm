for tc in range(int(input())):
    N, K = map(int, input().split())
    cnt = 0
    for i in range(1, 1<<12):
        bit_cnt = 0
        num_sum = 0
        for j in range(12):
            if i & (1 <<j):
                num_sum += j + 1
                bit_cnt += 1
        if num_sum ==K and bit_cnt == N:
            cnt += 1

    print('#{}'.format(tc + 1), cnt)