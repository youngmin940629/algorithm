for T in range(int(input())):
    H, W, N = map(int, input().split())
    hotel = [[0] * W for _ in range(H)]
    target_h = target_w = 0
    cnt = 0
    break_point = 0
    for x in range(W):
        for y in range(H):
            cnt += 1
            if cnt == N:
                target_w = x + 1
                target_h = y + 1
                break_point = 1
                break
        if break_point:
            break
    result = target_h * 100 + target_w
    print(result)