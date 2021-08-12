for tc in range(int(input())):
    N, K = map(int, input().split())
    square = [list(map(int, input().split())) for i in range(N)]
    cnt = 0
    for x in range(N):
        for y in range(N):
            tmp_idx = 0
            if square[y][x] == 1:
                for length in range(K):
                    if length == K-1:
                        if y + length + 1 < N and square[y + length + 1][x] == 1:
                            tmp_idx = 0
                    if y + length < N and square[y+length][x] == 1:
                        tmp_idx += 1
                    else:
                        break
                    if tmp_idx > K or y + length > N-1:
                        break
                if tmp_idx == K:
                    cnt += 1
    for y in range(N):
        for x in range(N):
            tmp_idx = 0
            if square[y][x] == 1:
                for length in range(K):
                    if length == K-1:
                        if x + length + 1 < N and square[y][x + length + 1] == 1:
                            tmp_idx = 0
                    if x + length < N and square[y][x+length] == 1:
                        tmp_idx += 1
                    else:
                        break
                    if tmp_idx > K or x + length > N-1:
                        break
                if tmp_idx == K:
                    cnt += 1
    print('#{}'.format(tc+1), cnt)