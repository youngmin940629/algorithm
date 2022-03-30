square_x = []
square_y = []
for _ in range(3):
    x,y = map(int, input().split())
    square_x.append(x)
    square_y.append(y)
for i in range(0,3):
    if square_x.count(square_x[i]) == 1:
        result_x = square_x[i]
    if square_y.count(square_y[i]) == 1:
        result_y = square_y[i]
print(result_x, result_y)