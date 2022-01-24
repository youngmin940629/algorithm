arr = [1] * (10001)
arr[0] = arr[1] = 0
num = 101
for number in range(2,num+1):
    if arr[number]:
        for i in range(number*2, 10001, number):
            arr[i] = 0

for tc in range(int(input())):
    N = int(input())
    for i in range(N//2, N):
        if arr[i] and arr[N-i]:
            a,b = min(i, N-i), max(i, N-i)
            break
    print(a,b)