def check(n):
    arr = [1] * (n * 2 + 1)
    arr[0] = arr[1] = 0
    num = int((2 * n) ** 0.5)
    for number in range(2,num+1):
        if arr[number]:
            for i in range(2*number, (2*n)+1, number):
                arr[i] = 0
    return sum(arr[n+1:2*n+1])
while True:
    N = int(input())
    if N == 0:
        break
    else:
        print(check(N))