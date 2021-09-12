N, X = map(int, input().split())
data = list(map(int, input().split()))
result = []
for idx in range(len(data)):
    if data[idx] < X:
        result.append(data[idx])
print(' '.join(map(str, result)))