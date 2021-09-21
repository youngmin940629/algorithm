data = [0] * 10000
result = 0
for num in range(10000):
    result = num
    while result < 10000:
        tmp_num = result
        while tmp_num > 0:
            result += (tmp_num % 10)
            tmp_num = tmp_num // 10
        if result < 10000:
            data[result] = 1
        if result == num:
            break
for idx in range(1,10000):
    if data[idx] == 0:
        print(idx)