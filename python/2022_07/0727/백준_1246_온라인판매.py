N, M = map(int, input().split())
array = []
for _ in range(M):
    array.append(int(input()))

array.sort()
result = 0
cost = 0
for i in range(len(array)):
    if len(array) - i <= N:
        tmp = array[i] * (len(array) - (i))
    else:
        tmp = array[i] * N
    if tmp > result:
        result = tmp
        cost = array[i]
print(cost, result)