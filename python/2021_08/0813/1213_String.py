for i in range(10):
    tc = int(input())
    check_str = input()
    test_str = input()
    result = 0
    for i in range(len(test_str)):
        cnt = 0
        if test_str[i] == check_str[0]:
            for check in range(len(check_str)):
                if i + check <len(test_str) and check_str[check] == test_str[i + check]:
                    cnt += 1
            if cnt == len(check_str):
                result += 1
    print('#{}'.format(tc), result)