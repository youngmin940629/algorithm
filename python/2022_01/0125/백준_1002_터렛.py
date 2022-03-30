T = int(input())
for _ in range(T):
    x1,y1,r1,x2,y2,r2 = map(int, input().split())
    dist = ((x1-x2) ** 2 + (y1-y2) ** 2) ** 0.5
    check = abs(r1+r2)
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if dist == check:
            print(1)
        elif dist > check:
            print(0)
        elif dist < check:
            check_r1 = max(r1,r2)
            check_r2 = min(r1,r2)
            if check_r1 == dist + check_r2:
                print(1)
            elif check_r1 < dist + check_r2:
                print(2)
            else:
                print(0)