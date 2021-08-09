cnt = 1
while cnt <= 10:
    N = int(input())
    print('#{}' .format(cnt), end = ' ')
    data = list(map(int, input().split()))
    result = 0
    for idx in range(2, N-2):
        tmp_view = 0
        view = 255
        for count in range(-2, 3):
            if data[idx] - data[idx + count] > 0:
                tmp_view = data[idx] - data[idx + count]
            else:
                if count == 0:
                    tmp_view = data[idx]
                else:
                    tmp_view = 0
            if tmp_view < view:
                view = tmp_view
        result += view
    print(result)
    cnt += 1