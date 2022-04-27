def findCommon(a,b):
    x, y = max(a,b) , min(a,b)
    while True:
        if x % y == 0:
            break
        else:
            x, y = y, x%y
    return y
N = int(input())
rings = list(map(int, input().split()))
for i in range(1, N):
    mod = findCommon(rings[0], rings[i])
    print(f'{int(rings[0]/mod)}/{int(rings[i]/mod)}')