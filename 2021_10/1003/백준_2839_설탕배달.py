N = int(input())
a = b = 0
for num in range(N // 5, -1, -1):
    a = num
    b = (N - (5 * a)) // 3
    if (5 * a) + (3 * b) == N:
        break
if (5 * a) + (3 * b) == N:
    print(a + b)
else:
    print(-1)