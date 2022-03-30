X = int(input())


def total_sum(n):
    return int((n*(n+1))/2)
cnt = 1
while total_sum(cnt) < X:
    cnt += 1

if cnt % 2:
    print('{}/{}'.format(total_sum(cnt) - X + 1 , X - total_sum(cnt-1)))
else:
    print('{}/{}'.format(X - total_sum(cnt - 1), total_sum(cnt) - X + 1))