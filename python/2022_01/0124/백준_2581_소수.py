def check(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2,n):
            if n % i == 0:
                return False
        return True

M = int(input())
N = int(input())
min_num = 0
result = 0
for num in range(M, N+1):
    if check(num):
        if min_num == 0:
            min_num = num
        result += num
if min_num == 0:
    print(-1)
else:
    print(result)
    print(min_num)