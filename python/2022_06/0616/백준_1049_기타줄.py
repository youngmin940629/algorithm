N, M = map(int,input().split())
brand = []
for _ in range(M):
    brand.append(list(map(int, input().split())))
value1, value2 = 0, 0
brand.sort(key=lambda x : x[0])
value1 = brand[0][0]
brand.sort(key=lambda x : x[1])
value2 = brand[0][1]
a1, a2 = N // 6 , N % 6
print(min(a1*value1 + a2*value2, (a1+1)*value1, value2*N))