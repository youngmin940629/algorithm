N = int(input())
num = '666'
cnt = 0
check = 0
while True:
    if num in str(cnt):
        check += 1
    cnt += 1
    if check == N:
        print(cnt-1)
        break
