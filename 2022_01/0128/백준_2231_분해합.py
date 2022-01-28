N = int(input())
tmp = N
count = 0
while True:
    tmp = tmp // 10
    count += 1
    if tmp == 0:
        break

flag = 0
check = N - (9 * count)
if check < 0:
    check = 0
for num in range(check, N):
    result = tmp = num
    while num != 0:
        tmp += num % 10
        num = num // 10
    if tmp == N:
        print(result)
        flag = 1
        break
if not flag:
    print(0)