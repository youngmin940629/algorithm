N = int(input())
arr = [list(input()) for _ in range(N)]
result = []
dx = [0, 0, 1, 1]
dy = [0, 1, 0, 1]
def check(x,y,n):
    check_arr = []
    global result
    for i in range(x, x+n):
        for j in range(y, y+n):
            check_arr.append(arr[i][j])
    
    if check_arr == ['0' for _ in range(n*n)]:
        result.append('0')
    elif check_arr == ['1' for _ in range(n*n)]:
        result.append('1')
    else:
        result.append('(')
        for dir in range(4):
            check(x+(dx[dir]* (n//2)), y+(dy[dir]*(n//2)), n//2 )
        result.append(')')

check(0,0,N)
print(''.join(map(str, result)))