for tc in range(int(input())):
    x, y = map(int,input().split())
    distance = y - x
    result = 0
    check_num = int(distance ** (1/2))
    check1 = distance - (check_num ** 2)
    check2 = (check_num + 1) ** 2 - distance
    if check1 == 0:
        result = check_num * 2 - 1
    elif check1 < check2:
        result = check_num * 2
    elif check1 > check2:
        result = check_num * 2 + 1
    print(result)