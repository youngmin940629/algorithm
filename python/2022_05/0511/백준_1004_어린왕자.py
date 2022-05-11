for tc in range(int(input())):
    st_x, st_y, end_x, end_y = map(int, input().split())
    result = 0
    for _ in range(int(input())):
        x, y, r = map(int, input().split())
        dist_st = (abs(st_x - x) ** 2 + abs(st_y-y) ** 2)
        dist_end = (abs(end_x - x) ** 2 + abs(end_y-y) ** 2)
        r = r**2
        if (dist_st < r and dist_end > r) or (dist_st > r and dist_end < r):
            result += 1
    print(result)