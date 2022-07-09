while True:
    n = int(input())
    if n == 0:
        break
    else:
        result = []
        n = n-1
        check = bin(n)[2:]
        length = len(check)
        for i in range(length):
            number = 3**(length - (i+1))*int(check[i])
            if number == 0:
                continue
            else:
                result.append(number)
        result.sort()
        if len(result) > 0:
            print('{ ' + ', '.join(map(str, result)) + ' }')
        else:
            print('{ }')