N = int(input())
P = list(map(int, input().split()))
P.sort()
result = 0
people = len(P)
for i in range(people):
    result += P[i] * (people-i)
print(result)