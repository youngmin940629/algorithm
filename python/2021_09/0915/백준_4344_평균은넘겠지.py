C = int(input())
for _ in range(C):
    data = list(map(int, input().split()))
    sum = 0
    for idx in range(1, len(data)):
        sum += data[idx]
    avg = sum/(len(data)-1)
    cnt = 0
    for idx in range(1, len(data)):
        if data[idx] > avg:
            cnt += 1
    print('{:.3f}%'.format((cnt/(len(data)-1))*100))