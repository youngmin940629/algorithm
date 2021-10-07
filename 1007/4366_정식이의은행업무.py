for tc in range(int(input())):
    bi = input()
    tri = input()
    bi_cnt = [0] * len(bi)
    tri_cnt = [0] * len(tri)
    check = []
    flag = 0
    result = 0
    for idx in range(len(bi)):
        bi_cnt[idx] = bi[len(bi)-idx-1]
    for idx in range(len(tri)):
        tri_cnt[idx] = tri[len(tri)-idx-1]

    for case in range(len(bi)):
        tmp_value = bi_cnt[case]
        for num in range(2):
            tmp = 0
            if int(bi_cnt[case]) != num:
                bi_cnt[case] = num
                for i in range(len(bi)):
                    tmp += 2 ** (i) * int(bi_cnt[i])
            check.append(tmp)
            bi_cnt[case] = tmp_value

    for case in range(len(tri)):
        tmp_value = tri_cnt[case]
        for num in range(3):
            tmp = 0
            if int(tri_cnt[case]) != num:
                tri_cnt[case] = num
                for i in range(len(tri)):
                    tmp += 3 ** (i) * int(tri_cnt[i])
                if tmp in check:
                    flag = 1
                    result = tmp
            tri_cnt[case] = tmp_value
        if flag == 1:
            break
    print('#{} {}'.format(tc+1, result))