N = int(input())
people = []
for _ in range(N):
    people.append(list(map(int, input().split())))

result = []
for i in range(N):
    tmp = 1
    for j in range(N):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            tmp += 1
    result.append(tmp)
print(' '.join(map(str, result)))