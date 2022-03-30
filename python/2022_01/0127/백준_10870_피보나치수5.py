def fibonachi(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        return fibonachi(N-1) + fibonachi(N-2)

n = int(input())
print(fibonachi(n))