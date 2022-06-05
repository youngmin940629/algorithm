N, K = map(int, input().split())
bag = [[0,0]]
for _ in range(N):
    W, V = map(int, input().split())
    bag.append([W,V])
knap = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,K+1):
        weight = bag[i][0]
        value = bag[i][1]

        if j < weight:
            knap[i][j] = knap[i-1][j]
        else:
            knap[i][j] = max(value + knap[i-1][j-weight], knap[i-1][j])
print(knap[N][K])