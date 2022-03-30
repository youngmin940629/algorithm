for tc in range(int(input())):
    number = float(input())
    result = ''
    while True:
        number *= 2
        if number > 1:
            number -= 1
            result += '1'
        elif number == 1:
            result += '1'
            break
        elif number < 1:
            result += '0'
        if len(result) > 12:
            result = 'overflow'
            break
    print('#{} {}'.format(tc+1, result))