def bi_tree(n):
    global cnt
    if n == 0:
        return
    bi_tree(left[n])
    cnt += 1
    node[n] = cnt
    bi_tree(right[n])

for tc in range(int(input())):
    N = int(input())
    left = [0] * (N+1)
    right = [0] * (N+1)
    node = [0] * (N+1)
    for i in range(2, N+1):
        if i % 2:
            right[i//2] = i
        else:
            left[i//2] = i
    cnt = 0
    bi_tree(1)
    print('#{} {} {}'.format(tc+1, node[1], node[N//2]))