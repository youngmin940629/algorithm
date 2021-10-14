def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]
def union(a, b):
    p[find_set(a)] = find_set(b)

for tc in range(int(input())):
    N, M = map(int, input().split())
    p = [i for i in range(N+1)]
    for _ in range(M):
        n1, n2 = map(int, input().split())
        union(n1, n2)
    result = set()
    for i in range(1,N+1):
        result.add(find_set(i))
    print('#{} {}'.format(tc+1, len(result)))