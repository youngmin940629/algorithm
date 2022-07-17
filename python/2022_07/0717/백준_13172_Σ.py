result = 0
def ans(n,s):
    return s*mul(n,1000000007-2)%1000000007
def mul(b,t):
    if t == 1:
        return b%1000000007
    if t % 2 == 0:
        tmp = mul(b, t//2)
        return (tmp**2)%1000000007
    else:
        return b*mul(b,t-1)%1000000007
for _ in range(int(input())):
    n, s = map(int,input().split())
    result += ans(n,s)
    result %= 1000000007
print(result)