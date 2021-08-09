case = int(input())
cnt = 1
while cnt <= case:
    print('#{}' .format(cnt), end = ' ')
    N = int(input())
    data = list(map(int, input().split()))
    for idx in range(len(data) - 1, 0, -1):
        for compare_idx in range(0, idx):
            if data[compare_idx] > data[compare_idx+1]:
                data[compare_idx], data[compare_idx+1] = data[compare_idx+1], data[compare_idx]
    for num in range(0, N):
        print(data[num], end = ' ')
    print()
    cnt += 1