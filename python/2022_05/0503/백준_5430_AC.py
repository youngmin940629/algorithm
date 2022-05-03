import sys

input = sys.stdin.readline

for tc in range(int(input())):
    p = input().rstrip()
    n = int(input().rstrip())
    if n == 0:
        tmp = input()
        arr = []
    else:
        arr = list(map(int, input()[1:-2].split(',')))
    f,r = 0,0
    mode = True
    for word in p:
        if word == 'R':
            mode = not mode
        else:
            if mode == True:
                f += 1
            else:
                r += 1
    if len(arr) == 0 and f == 0 and r == 0:
        print('[]')
    else:
        if len(arr) - (f+r) < 0:
            print('error')
        elif len(arr) - (f+r) == 0:
            print('[]')
        else:
            if mode == True:
                print(str(arr[f:n-r]).replace(" ", ''))
            else:
                arr.reverse()
                print(str(arr[r:n-f]).replace(" ", ''))