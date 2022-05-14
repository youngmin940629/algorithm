W, H, X, Y, P = map(int, input().split())
result = 0
sq_x1, sq_y1, sq_x2, sq_y2 =  X, Y, X+W, Y+H
c1_x, c1_y, c2_x, c2_y = X, Y+H//2 , X+W, Y+H//2
for _ in range(P):
    x, y = map(int, input().split())
    if sq_x1 <= x <= sq_x2 and sq_y1 <= y <= sq_y2:
        result += 1
    else:
        if (H // 2)**2 >= abs(x-c1_x) ** 2 + abs(y-c1_y) ** 2:
            result += 1
        elif (H // 2)**2 >= abs(x-c2_x) ** 2 + abs(y-c2_y) ** 2:
            result += 1
print(result)