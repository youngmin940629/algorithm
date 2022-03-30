for _ in range(int(input())):
    brackets = input()
    check = 0
    for bracket in brackets:
        if bracket == '(':
            check += 1
        else:
            check -= 1
        if check < 0:
            break
    if check == 0:
        print('YES')
    else:
        print('NO')