def binary_check(arr, k, l, r, flag):
    global cnt
    if l <= r:
        m = (l + r) // 2
        if k == arr[m]:
            cnt += 1
        elif k < arr[m]:
            if flag == -1:
                return
            else:
                flag = -1
                return binary_check(arr, k, l, m-1, flag)
        else:
            if flag == 1:
                return
            else:
                flag = 1
                return binary_check(arr, k, m+1, r, flag)

for tc in range(int(input())):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    cnt = 0
    A.sort()
    for check in B:
        flag = 0
        binary_check(A, check, 0, len(A)-1, flag)
    print('#{} {}'.format(tc+1, cnt))