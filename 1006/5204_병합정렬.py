def merge_sort(arr):
    if len(arr) == 1:
        return arr
    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    return merge(left,right)

def merge(l, r):
    global cnt
    result = [0] * (len(l) + len(r))
    len_l = len(l)
    len_r = len(r)
    idx = idx_l = idx_r = 0
    while idx_l < len_l and idx_r < len_r:
        if l[idx_l] <= r[idx_r]:
            result[idx] = l[idx_l]
            idx += 1
            idx_l += 1
        else:
            result[idx] = r[idx_r]
            idx += 1
            idx_r += 1
    if idx_l == len_l:
        for i in range(idx_r, len_r):
            result[idx] = r[i]
            idx += 1
    elif idx_r == len_r:
        cnt += 1
        for i in range(idx_l, len_l):
            result[idx] = l[i]
            idx += 1
    return result

for tc in range(int(input())):
    N = int(input())
    data = list(map(int, input().split()))
    cnt = 0
    print('#{} {} {}'.format(tc+1, merge_sort(data)[N//2],cnt))