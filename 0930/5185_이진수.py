for tc in range(int(input())):
    N, num = input().split()
    result = ''
    for number in num:
        if number == 'A':
            number = 10
        elif number == 'B':
            number = 11
        elif number == 'C':
            number = 12
        elif number == 'D':
            number = 13
        elif number == 'E':
            number = 14
        elif number == 'F':
            number = 15
        else:
            number = int(number)
        output = ''
        for i in range(3, -1, -1):
            if number & (1 << i):
                output += '1'
            else:
                output += '0'
        result += output
    print('#{} {}'.format(tc+1, result))