# import sys
# sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input().strip() for _ in range(N)]
    oct = {
        '0':'0000', '1':'0001', '2':'0010', '3':'0011',
        '4':'0100', '5':'0101', '6':'0110', '7':'0111',
        '8':'1000', '9':'1001', 'A':'1010', 'B':'1011',
        'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'
    }
    code = {
        '112' : 0,
        '122' : 1,
        '221' : 2,
        '114' : 3,
        '231' : 4,
        '132' : 5,
        '411' : 6,
        '213' : 7,
        '312' : 8,
        '211' : 9
    }
    result = 0
    for i in range(N):
        decode = ''
        for idx in arr[i]:
            decode += oct[idx]
        arr[i] = decode
        decode = ''
    password = []
    visited = []
    for i in range(N):
        if '1' in arr[i]:
            c1 = c2 = c3 = 0
            for check in range(len(arr[i])-1, -1, -1):
                if c2 == 0 and c3 == 0 and arr[i][check] == '1':
                    c1 += 1
                elif c1 != 0 and c3 == 0 and arr[i][check] == '0':
                    c2 += 1
                elif c1 * c2 != 0 and arr[i][check] == '1':
                    c3 += 1
                elif c3 != 0 and arr[i][check] == '0':
                    n = min(c1, c2, c3)
                    password.append(code[str(int(c1//n)) + str(int(c2//n)) + str(int(c3/n))])
                    c1 = c2 = c3 = 0
                    key = ''
                    if len(password) == 8:
                        if password not in visited:
                            if ((password[0] + password[2] + password[4] + password[6]) + (password[1] + password[3] + password[5] + password[7]) * 3) % 10 == 0:
                                result += password[0] + password[2] + password[4] + password[6] + password[1] + password[3] + password[5] + password[7]
                            visited.append(password)
                        password = []
    print('#{} {}'.format(tc, result))