def check_dessert(x,y,dir,cnt):
    global result, st_x, st_y
    if dir == 3 and x == st_x and y == st_y:
        result = max(result, cnt)
        return
    if x < 0 or x >= N or y < 0 or y >= N or dessert[x][y] in trace:
        return
    else:
        trace.append(dessert[x][y])
        if dir == 0:
            check_dessert(x+dx[dir], y+dy[dir], dir, cnt+1)
            check_dessert(x+dx[dir+1], y+dy[dir+1], dir+1, cnt+1)
        elif dir == 1:
            check_dessert(x + dx[dir], y + dy[dir], dir, cnt + 1)
            check_dessert(x + dx[dir + 1], y + dy[dir + 1], dir + 1, cnt + 1)
        elif dir == 2:
            if x+y == st_x+st_y:
                check_dessert(x + dx[dir + 1], y + dy[dir + 1], dir + 1, cnt + 1)
            else:
                check_dessert(x + dx[dir], y + dy[dir], dir, cnt + 1)
        elif dir == 3:
            check_dessert(x + dx[dir], y + dy[dir], dir, cnt+1)
        trace.pop()
for tc in range(int(input())):
    N = int(input())
    dessert = [list(map(int, input().split())) for _ in range(N)]
    dx = [1, -1, -1, 1]
    dy = [1, 1, -1, -1]
    result = -1
    trace = []
    for x in range(1, N-1):
        for y in range(0, N-2):
            st_x, st_y = x, y
            trace.append(dessert[x][y])
            check_dessert(x+1,y+1,0,1)
            trace.pop()
    print('#{} {}'.format(tc+1, result))