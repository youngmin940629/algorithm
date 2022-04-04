arr = list(map(int, input().split()))
tmp = arr[0]
check = 0
for i in range(1, len(arr)):
    if arr[i] > tmp:
        check += 1
    if arr[i] < tmp:
        check -= 1
    tmp = arr[i]
if check == 7:
    print('ascending')
elif check == -7:
    print('descending')
else:
    print('mixed')