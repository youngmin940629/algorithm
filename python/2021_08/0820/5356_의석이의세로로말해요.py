for tc in range(int(input())):
    data = [list(map(str, input())) for _ in range(5)]
    len_max = 0
    result = []
    for idx in range(5):
        if len(data[idx]) > len_max:
            len_max = len(data[idx])
    for idx in range(5):
        if len_max > len(data[idx]):
            for add in range(len_max-len(data[idx])):
                data[idx] = data[idx] + ['*']
    for x in range(len_max):
        for y in range(5):
            result = result + [data[y][x]]
    print('#{} '.format(tc+1), end = '')
    for idx in range(len(result)):
        if result[idx] == '*':
            continue
        else:
            print(result[idx], end = '')
    print()