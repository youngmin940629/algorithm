data = list(map(int, input().split()))
result = 0
for idx in range(len(data)):
    result += data[idx]
print(result)