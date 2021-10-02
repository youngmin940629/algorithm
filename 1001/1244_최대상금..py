def change(idx, cnt):
    global M, result
    if cnt == M:
        if result < int("".join(N)):
            result = int("".join(N))
        return
    for i in range(idx, length):
        for j in range(i + 1, length):
            if int(N[i]) <= int(N[j]):
                N[i] , N[j] = N[j], N[i]
                change(i ,cnt + 1)
                N[i], N[j] = N[j], N[i]

for tc in range(int(input())):
    N, M = input().split()
    N, M, length = list(N), int(M), len(N)
    result = int("".join(N))
    check_cnt = 1
    for i in range(length-1):
        if int(N[i]) > int(N[i+1]):
            check_cnt += 1
    if check_cnt == length:
        if M % 2 == 1:
            N[-1], N[-2] = N[-2], N[-1]
            result = int("".join(N))
    else:
        change(0,0)
    print('#{} {}'.format(tc+1, result))