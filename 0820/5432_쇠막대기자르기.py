for tc in range(int(input())):
    a = input()
    b = a.replace("()", '/')
    stick = 0
    result = 0
    for idx in range(len(b)):
        if b[idx] == '(':
            stick += 1
        elif b[idx] == ')':
            result += 1
            stick -= 1
        elif b[idx] =='/':
            result += stick
    print('#{} {}'.format(tc+1, result))