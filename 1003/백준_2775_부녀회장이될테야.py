for tc in range(int(input())):
    k = int(input())
    n = int(input())
    result = 1
    for i in range(k+1):
        result *= (n+k-i)
    for j in range(1,k+2):
        result = int(result / j)
    print(result)