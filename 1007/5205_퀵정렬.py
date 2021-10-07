def quicksort(arr, l, r):
    if l < r:
        s = partition(arr, l, r)
        quicksort(arr, l, s-1)
        quicksort(arr, s+1, r)
def partition(arr, l, r):
    p = arr[l]
    i = l
    j = r
    while i <= j:
        while i < j and arr[i] <= p:
            i += 1
        while l < j and arr[j] >= p:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        if i == j:
            break
    arr[l], arr[j] = arr[j], arr[l]
    return j

for tc in range(int(input())):
    N = int(input())
    data = list(map(int, input().split()))
    quicksort(data, 0, len(data)-1)
    print('#{} {}'.format(tc+1, data[N//2]))