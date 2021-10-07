def binarySearch(Page, key):
    start, end = 1, Page
    cnt = 0
    if key == start or key == end:
        return 1
    while start <= end:
        middle = int((start + end)/2)
        cnt += 1
        if middle == key:
            return cnt
        elif middle > key:
            end = middle
        else:
            start = middle

for tc in range(int(input())):
    P, A, B = map(int, input().split())
    cnt_A = binarySearch(P, A)
    cnt_B = binarySearch(P, B)
    if cnt_A < cnt_B:
        result = 'A'
    elif cnt_A > cnt_B:
        result = 'B'
    else:
        result = 0
    print('#{}'.format(tc + 1), result)
