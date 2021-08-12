import sys
sys.stdin = open('input.txt','r')

for tc in range(10):
    N = int(input())
    ladder = [list(map(int, input().split())) for i in range(100)]
    result = 0
    y = 0
    for start in range(100):
        if ladder[0][start] == 1:
            tmp_start = start
            x = start
            y = 0
            while y < 99:
                if x + 1 < 100 and ladder[y][x + 1] == 1:
                    x = x + 1
                    while ladder[y+1][x] != 1:
                        x = x + 1
                    y = y + 1
                elif x - 1 >= 0 and ladder[y][x - 1] == 1:
                    x = x - 1
                    while ladder[y+1][x] != 1:
                        x = x - 1
                    y = y + 1
                else:
                    y = y + 1
            if ladder[y][x] == 2:
                result = tmp_start
                break
    print('#{}' .format(N), result)