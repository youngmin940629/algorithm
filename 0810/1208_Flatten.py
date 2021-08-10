cnt = 1
while cnt <= 10:
    N = int(input())
    data = list(map(int, input().split()))
    for flat_cnt in range(0, N):
        max_value = data[0]
        min_value = data[0]
        max_idx = 0
        min_idx = 0
        for idx in range(0, 100):
            if max_value < data[idx]:
                max_value = data[idx]
                max_idx = idx
            if min_value > data[idx]:
                min_value = data[idx]
                min_idx = idx
        data[max_idx] -= 1
        data[min_idx] += 1
    max_value = data[0]
    min_value = data[0]
    max_idx = 0
    min_idx = 0
    for idx in range(0, 100):
        if max_value < data[idx]:
            max_value = data[idx]
            max_idx = idx
        if min_value > data[idx]:
            min_value = data[idx]
            min_idx = idx
    print('#{} ' .format(cnt), max_value - min_value)
    cnt += 1