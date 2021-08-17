for tc in range(int(input())):
    N, M = map(int, input().split())
    data = [list(input()) for _ in range(N)]
    result = []
    for x in range(N):
        if result != []:
            break
        else:
            for y in range(N-M+1):
                check_cnt = 0
                for check in range(M//2):
                    if data[y+check][x] == data[y+M-check-1][x]:
                        check_cnt += 1
                    else:
                        break
                if check_cnt == M//2:
                    for idx in range(M):
                        result += data[y+idx][x]
                    break
    for y in range(N):
        if result != []:
            break
        else:
            for x in range(N-M+1):
                check_cnt = 0
                for check in range(M//2):
                    if data[y][x+check] == data[y][x+M-check-1]:
                        check_cnt += 1
                    else:
                        break
                if check_cnt == M//2:
                    for idx in range(M):
                        result += data[y][x + idx]
                    break
    print('#{}'.format(tc+1), ''.join(map(str, result)))