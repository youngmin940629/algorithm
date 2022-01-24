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

N = int(input())
arr = list(map(int, input().split()))
result = 0
for num in arr:
    if check(num):
        result += 1
print(result)