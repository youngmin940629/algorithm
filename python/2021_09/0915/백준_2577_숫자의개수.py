mul = 1
for _ in range(3):
    n = int(input())
    mul *= n
result = [0] * 10
while mul > 0:
    result[(mul % 10)] += 1
    mul = mul // 10
for idx in range(10):
    print(result[idx])