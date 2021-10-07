arr = list('algorithm')
N = len(arr)
for i in range(N // 2):
    arr[i], arr[N - 1 - i] = arr[N - 1 - i], arr[i]