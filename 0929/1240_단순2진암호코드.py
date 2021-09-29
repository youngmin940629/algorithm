for tc in range(int(input())):
    N, M = map(int, input().split())
    data = [list(input()) for _ in range(N)]
    code = {
        '0001101' : 0,
        '0011001' : 1,
        '0010011' : 2,
        '0111101' : 3,
        '0100011' : 4,
        '0110001' : 5,
        '0101111' : 6,
        '0111011' : 7,
        '0110111' : 8,
        '0001011' : 9,
    }
    password = ''
    check_idx = 0
    end_idx = 0
    result = []
    result_check = 0
    result_sum = 0
    for i in range(N):
        if '1' in data[i]:
            check_idx = i
            break
    for idx in range(M-1, -1, -1):
        if data[check_idx][idx] == '1':
            end_idx = idx
            break
    for pwd_idx in range(55, -1, -1):
        password += data[check_idx][end_idx - pwd_idx]
    for check in range(0, 56, 7):
        result.append(code[password[check:check+7]])
    for idx in range(8):
        if idx % 2:
            result_check += result[idx]
        else:
            result_check += result[idx] * 3
        result_sum += result[idx]
    if result_check % 10:
        print('#{} {}'.format(tc+1, 0))
    else:
        print('#{} {}'.format(tc+1, result_sum))