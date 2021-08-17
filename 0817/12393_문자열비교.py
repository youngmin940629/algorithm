for tc in range(int(input())):
    A = input()
    B = input()
    cnt = 0
    for idx in range(len(B)-len(A)+1):
        check_cnt = 0
        if A[0] == B[idx]:
            for check_idx in range(len(A)):
                if A[check_idx] == B[idx + check_idx]:
                    check_cnt += 1
                else:
                    break
        if check_cnt == len(A):
            cnt += 1
    print('#{}'.format(tc+1), cnt)
