def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

def distance(x_arr, y_arr):
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            ret = (((x_arr[i]-x_arr[j]) ** 2) + ((y_arr[i]-y_arr[j]) ** 2))
            edges.append((i,j,ret))

for tc in range(int(input())):
    N = int(input())
    x = [0] + list(map(int, input().split()))
    y = [0] + list(map(int, input().split()))
    E = float(input())
    p = [i for i in range(N+1)]
    edges = []
    distance(x,y)
    edges.sort(key=lambda x: x[2], reverse=True)
    cnt = N - 1
    ans = 0
    while cnt:
        u, v, w = edges.pop()
        a = find_set(u)
        b = find_set(v)
        if a == b: continue
        p[b] = a
        ans += w
        cnt -= 1
    print('#{} {:.0f}'.format(tc+1, ans*E))