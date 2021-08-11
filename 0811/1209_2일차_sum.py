import sys
sys.stdin = open('input.txt', 'r')

for tc in range(10):
    num = int(input())
    arr = [list(map(int, input().split())) for i in range(100)]
    total = 0
    for x in range(100):
        tmp_total = 0
        for y in range(100):
            tmp_total += arr[x][y]
        if total < tmp_total:
            total = tmp_total
    for y in range(100):
        tmp_total = 0
        for x in range(100):
            tmp_total += arr[x][y]
        if total < tmp_total:
            total = tmp_total
    for cnt in range(2):
        tmp_total = 0
        if cnt == 0:
            for diag_cnt in range(100):
                tmp_total += arr[diag_cnt][diag_cnt]
            if total < tmp_total:
                total = tmp_total
        if cnt == 1:
            for diag_cnt in range(100):
                tmp_total += arr[99-diag_cnt][diag_cnt]
            if total < tmp_total:
                total = tmp_total
    print('#{}'.format(num), total)