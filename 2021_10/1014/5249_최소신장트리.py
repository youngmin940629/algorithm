def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]
for tc in range(int(input())):
    V, E = map(int, input().split())
    edges = []
    for _ in range(E):
        edges.append(tuple(map(int, input().split())))
    p = [i for i in range(V+1)]
    edges.sort(key=lambda x: x[2], reverse=True)
    cnt = V
    ans = 0
    while cnt:
        u, v, w = edges.pop()
        a = find_set(u)
        b = find_set(v)
        if a == b: continue
        p[b] = a
        ans += w
        cnt -= 1
    print('#{} {}'.format(tc+1, ans))