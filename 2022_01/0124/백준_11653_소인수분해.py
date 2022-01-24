N = int(input())
n = 2
if N != 1:
    while N != 1:
        if N % n == 0:
            N = N // n
            print(n)
        else:
            n += 1