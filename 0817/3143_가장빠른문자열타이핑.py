for tc in range(int(input())):
    A, B = input().split()
    cnt = 0
    check = 0
    while check < (len(A) - len(B) + 1):
        check_cnt = 0
        if A[check] == B[0]:
            for idx in range(len(B)):
                if A[check+idx] == B[idx]:
                    check_cnt += 1
                else:
                    break
        if check_cnt == len(B):
            cnt += 1
            check += len(B)
        else:
            check += 1
    result = len(A) - (len(B) - 1) * cnt
    print('#{} {}'.format(tc+1, result))