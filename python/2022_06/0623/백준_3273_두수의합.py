n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()

left, right = 0, n-1
result = 0
while left < right:
    tmp = arr[left] + arr[right]
    if tmp == x:
        result += 1
    if tmp < x:
        left += 1
        continue
    right -= 1
print(result)