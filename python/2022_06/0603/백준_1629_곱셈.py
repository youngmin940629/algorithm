def speed_pow(x, y, z):
    if y == 1:
        return x%z
    else:
        k = speed_pow(x, y//2, z)
        if y % 2 == 0:
            return k*k%z
        else:
            return k*k*x%z


A, B, C = map(int, input().split())
print(speed_pow(A, B, C))