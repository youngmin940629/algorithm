def search(a):
    global cnt
    if a == 0:
        return
    cnt += 1
    search(left[a])
    search(right[a])

for tc in range(int(input())):
    E, N = map(int, input().split())
    tree = list(map(int, input().split()))
    left = [0] * (E+2)
    right = [0] * (E+2)
    for idx in range(0, len(tree), 2):
        if left[tree[idx]] == 0:
            left[tree[idx]] = tree[idx+1]
        else:
            right[tree[idx]] = tree[idx+1]
    cnt = 0
    search(N)
    print('#{} {}'.format(tc+1, cnt))