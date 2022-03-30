N = int(input())
num = int(input())
result = 0
while num > 0:
    result += num % 10
    num = num // 10
print(result)