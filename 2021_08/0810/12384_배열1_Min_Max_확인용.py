case = int(input())
cnt = 1
while case >= cnt:
    print('#%d' %cnt, end = ' ')
    N = int(input())
    data = list(map(int, input().split()))
    min_num = data[0]
    max_num = data[0]
    for idx in range(0, N):
        if min_num > data[idx]:
            min_num = data[idx]
        if max_num < data[idx]:
            max_num = data[idx]
    print(max_num - min_num)
    cnt += 1