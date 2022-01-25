while True:
    a,b,c = map(int,input().split())
    if a == 0 and b == 0 and c == 0:
        break
    else:
        square = [a,b,c]
        square.sort()
        if square[0] ** 2 + square[1] ** 2 == square[2] ** 2:
            print('right')
        else:
            print('wrong')