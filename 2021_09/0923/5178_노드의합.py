for tc in range(int(input())):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    for _ in range(M):
        a, b = map(int,input().split())
        tree[a] = b
        if a % 2:
            right[a] = b
        else:
            left[a] = b
    for idx in range(N - M, 0, -1):
        if idx * 2 <= N:
            tree[idx] += left[idx * 2]
        if idx * 2 + 1 <= N:
            tree[idx] += right[idx * 2 + 1]
        if idx % 2:
            right[idx] = tree[idx]
        else:
            left[idx] = tree[idx]
    print('#{} {}'.format(tc+1, tree[L]))