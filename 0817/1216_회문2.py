import sys
sys.stdin = open('input.txt','r')

for tc in range(10):
    case = int(input())
    data = [list(map(str, input())) for _ in range(100)]
    max = 1
    for y in range(100):
        for x in range(99):
            tmp_max = 1
            for check in range(2, 101-x):
                for check_idx in range(check//2):
                    if data[y][x+check_idx] == data[y][x+check-check_idx-1]:
                        tmp_max = check
                    else:
                        tmp_max = 1
                        break
                if max < tmp_max:
                    max = tmp_max
    for x in range(100):
        for y in range(99):
            tmp_max = 1
            for check in range(2, 101-y):
                for check_idx in range(check//2):
                    if data[y+check_idx][x] == data[y+check-check_idx-1][x]:
                        tmp_max = check
                    else:
                        tmp_max = 1
                        break
                if max < tmp_max:
                    max = tmp_max
    print("#{} {}".format(tc+1, max))