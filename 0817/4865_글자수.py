for tc in range(int(input())):
    str1 = input()
    str2 = input()
    data = dict()
    max = 0
    for word in str1:
        data[word] = 0
    for key in data:
        for find in str2:
            if key == find:
                data[key] += 1
    for key in data:
        if data[key] > max:
            max = data[key]
    print('#{}'.format(tc+1), max)