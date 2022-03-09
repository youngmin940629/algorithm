n = int(input())
stack = []
arr = []
count = 1
tmp = True
for i in range(n):
    num = int(input())
    while count <= num:
        stack.append(count)
        arr.append('+')
        count += 1
    if stack[-1] == num:
        stack.pop()
        arr.append('-')
    else:
        tmp = False
if not tmp:
    print('NO')
else:
    for i in arr:
        print(i)