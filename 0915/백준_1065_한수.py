N = int(input())
cnt = 0
for num in range(1, N+1):
    data = []
    for i in str(num):
        data.append(i)
    data = list(map(int, data))
    if len(data) <= 2:
        cnt += 1
    else:
        if data[0] - data[1] == data[1] - data[2]:
            cnt += 1
print(cnt)