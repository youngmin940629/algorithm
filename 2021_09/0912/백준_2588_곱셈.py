A = int(input())
B = int(input())
result = 0
for i in range(3):
    C = A * (B % 10)
    print(C)
    B = B // 10
    result = result + (C * (10**(i)))
print(result)