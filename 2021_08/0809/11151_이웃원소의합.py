case = int(input())
cnt = 1
while cnt <= case:
    print('#{}' .format(cnt), end = ' ')
    N = int(input())
    data = list(map(int, input().split()))
    tmp_result = 0
    result = data[0] + data[1]
    for idx in range(0, N-1):
        tmp_result = data[idx] + data[idx + 1]
        if tmp_result > result:
            result = tmp_result
    print(result)
    cnt += 1