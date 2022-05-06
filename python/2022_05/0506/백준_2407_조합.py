n, m = map(int, input().split())
result= 1
m = min(m, n-m)
if n == m:
    result = 1
else:
    for i in range(n, n-m , -1):
        result *= i
        print(i)
    for j in range(1,m+1):
        result /= j
        print(j)
print(int(result))


import math

n, m = map(int, input().split())
up = math.factorial(n)
down = (math.factorial(n - m)) * (math.factorial(m))
print(up // down)

