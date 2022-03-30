for tc in range(int(input())):
    N = int(input())
    num_list = list(map(int, input().split()))
    mode = 0
    result = []
    for i in range(N):
        max_num = 1
        min_num = 100
        tmp_idx = 0
        if mode == 0:
            for idx in range(N):
                if num_list[idx] != 101 and max_num < num_list[idx]:
                    max_num = num_list[idx]
                    tmp_idx = idx
            result = result + [max_num]
            num_list[tmp_idx] = 0
            mode = 1
        elif mode == 1:
            for idx in range(N):
                if num_list[idx] != 0 and min_num > num_list[idx]:
                    min_num = num_list[idx]
                    tmp_idx = idx
            result = result + [min_num]
            num_list[tmp_idx] = 101
            mode = 0
    print('#{}'.format(tc + 1), ' '.join(map(str, result[0:10])))