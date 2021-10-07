for tc in range(int(input())):
    N, M = map(int, input().split())
    bit = [0] * 30
    for idx in range(30):
        if M & (1 << idx):
            bit[idx] = 1
    result = 'ON'
    for check in range(N):
        if bit[check] == 0:
            result = 'OFF'
            break
    print('#{} {}'.format(tc+1, result))