case = int(input())
cnt = 1
while case >= cnt:
    print('#{}' .format(cnt), end = ' ')
    N = int(input())
    data = str(input())
    count_list = [0] * 10
    max_num = 0
    max_idx = 0
    for idx in range(0, N):
        count_list[int(data[idx])] += 1
    for idx in range(0, 10):
        if max_num < count_list[idx]:
            max_num = count_list[idx]
            max_idx = idx
        elif max_num == count_list[idx]:
            if max_idx < idx:
                max_idx = idx
    print(max_idx, max_num)
    cnt += 1