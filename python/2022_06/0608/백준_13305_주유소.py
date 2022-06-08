N = int(input())
dist = list(map(int,input().split()))
cost = list(map(int,input().split()))

for i in range(len(dist)-2, -1, -1):
    dist[i] = dist[i] + dist[i+1]

check = []
for i in range(len(cost)-1):
    check.append([i,cost[i]])
check.sort(key = lambda x : x[1])

min_idx =check[0][0]
cost_check = [check[0]]
for value in check:
    if min_idx > value[0]:
        cost_check.append(value)
        min_idx = value[0]
    if min_idx == 0:
        break
result = 0
for i in range(len(cost_check)):
    if i == 0:
        idx, idx_cost = cost_check[i][0], cost_check[i][1]
        result += (idx_cost * dist[idx])
    else:
        ex_idx = idx
        idx, idx_cost = cost_check[i][0], cost_check[i][1]
        result += (idx_cost * (dist[idx]-dist[ex_idx]))
print(result)