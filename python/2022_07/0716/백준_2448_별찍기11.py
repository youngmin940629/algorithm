M = int(input())
star = [[' ' for _ in range(M*2)] for _ in range(M)]

def go(x, y, n):
    if n <= 3:
        for i in range(3):
            for j in range(i+1):
                star[x+i][y+j] = star[x+i][y-j] = '*'
        star[x+1][y] = ' '
        return
    m = n // 2
    go(x, y, m)
    go(x+m, y-m, m)
    go(x+m, y+m, m)

go(0, M-1, M)

for i in range(M):
    print("".join(star[i]))