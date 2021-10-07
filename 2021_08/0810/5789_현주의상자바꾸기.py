cnt = 1
case1 = int(input())
while cnt <= case1:
    test_case = list(map(int, input().split()))
    box = [0] * test_case[0]
    num_cnt = 1
    while num_cnt <= test_case[1]:
        case = list(map(int, input().split()))
        for box_idx in range(case[0] - 1, case[1]):
            box[box_idx] = num_cnt
        num_cnt += 1
    print('#{}'.format(cnt), ' '.join(map(str, box)))
    cnt += 1