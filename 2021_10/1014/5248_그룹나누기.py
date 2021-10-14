def union(a, b):
    parent[find_set(a)] = find_set(b)

def find_set(u):
    if u == parent[u]:
        return u
    else:
        return find_set(parent[u])

for tc in range(int(input())):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    parent = [i for i in range(N+1)]
    for idx in range(0, len(data), 2):
        union(data[idx], data[idx+1])
    result = set()
    for idx in range(1, N+1):
        result.add(find_set(idx))
    print('#{} {}'.format(tc+1, len(result)))