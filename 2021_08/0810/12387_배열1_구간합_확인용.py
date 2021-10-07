case = int(input())
cnt = 1
while cnt <= case:
    data = list(map(int, input().split()))
    data_list = list(map(int, input().split()))
    min_value = 0
    max_value = 0
    for init_idx in range(0, data[1]):
        min_value += data_list[init_idx]
        max_value += data_list[init_idx]
    for sum_count in range(0, data[0] - data[1] + 1):
        tmp_min = 0
        for sum_idx in range(0, data[1]):
            tmp_min += data_list[sum_count + sum_idx]
        if tmp_min < min_value:
            min_value = tmp_min
    for sum_count in range(0, data[0] - data[1] + 1):
        tmp_max = 0
        for sum_idx in range(0, data[1]):
            tmp_max += data_list[sum_count + sum_idx]
        if tmp_max > max_value:
            max_value = tmp_max
    print('#{}' .format(cnt), max_value - min_value)
    cnt += 1