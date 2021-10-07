N = int(input())
def bee(n):
    return int(1+((n*(n-1))/2)*6)
cnt = 1
while bee(cnt) < N:
    cnt += 1

print(cnt)