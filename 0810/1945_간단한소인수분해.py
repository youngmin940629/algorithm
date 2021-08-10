T = int(input())
cnt = 1
while cnt <= T:
    number = int(input())
    data = [0] * 5
    while number > 1:
        if number % 2 == 0:
            data[0] += 1
            number = number / 2
        elif number % 3 == 0:
            data[1] += 1
            number = number / 3
        elif number % 5 == 0:
            data[2] += 1
            number = number / 5
        elif number % 7 == 0:
            data[3] += 1
            number = number / 7
        elif number % 11 == 0:
            data[4] += 1
            number = number / 11
    print('#{}'.format(cnt), ' '.join(map(str,data)))
    cnt += 1