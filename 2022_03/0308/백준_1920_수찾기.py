N = int(input())
arr1 = sorted(list(map(int, input().split())))
M = int(input())
arr2 = list(map(int,input().split()))

def binary(l, n, start, end):
    if start > end:
        return 0
    m = (start + end) // 2
    if l == n[m]:
        return 1
    elif l < n[m]:
        return binary(l, n, start, m-1)
    else:
        return binary(l,n,m+1,end)

for num in arr2:
    start = 0
    end = len(arr1) - 1
    print(binary(num, arr1, start, end))