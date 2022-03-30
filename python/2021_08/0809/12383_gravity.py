case = int(input())
cnt = 1
while cnt <= case:
    print('#{}' .format(cnt), end = ' ')
    N = int(input())
    data = list(map(int, input().split()))
    tmp_result = 0
    result = 0
    for num in data:
        big_num = 0
        for idx in range(data.index(num), N):
            if num <= data[idx]:
                big_num += 1
            tmp_result = N - data.index(num) - big_num
        if tmp_result > result:
            result = tmp_result
    print(result)
    cnt += 1