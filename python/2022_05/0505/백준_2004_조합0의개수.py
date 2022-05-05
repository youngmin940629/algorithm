n, m = map(int, input().split())

def a_count(a,num):
    result = 0
    tmp = a
    while num >= a:
        result += (num//a)
        a *= tmp
    return result

print(min(a_count(2,n) - a_count(2,m) - a_count(2,n-m),a_count(5,n) - a_count(5,m) - a_count(5,n-m)))