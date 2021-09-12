N = int(input())
first = N
cnt = 0
while True:
    num = (N % 10)
    N = (N // 10) + (N % 10)
    N = (N % 10) + (num * 10)
    cnt += 1
    if first == N:
        break
print(cnt)