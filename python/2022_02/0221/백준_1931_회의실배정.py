N = int(input())
time = []
for _ in range(N):
    time.append(list(map(int, input().split())))
time.sort()
time.sort(key = lambda x: x[1])
result = 0
end = 0
for i in time:
    if i[0] >= end:
        end = i[1]
        result += 1
print(result)