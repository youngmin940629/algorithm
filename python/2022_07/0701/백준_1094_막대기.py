X = int(input())
result = 0
tmp = 64
while X > 0:
    if X >= tmp:
        result += 1
        X -= tmp
    elif X < tmp:
        tmp = tmp // 2
print(result)