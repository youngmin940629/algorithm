N = int(input())
arr1 = list(map(int, input().split()))
arr1.sort()
M = int(input())
arr2 = list(map(int, input().split()))
result = [0] * M
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None
for i in range(M):
    if binary_search(arr1, arr2[i], 0, N-1) is not None:
        result[i] = 1
print(' '.join(map(str, result)))