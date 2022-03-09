N = int(input())
people = []
for _ in range(N):
    people.append(input().split())
people.sort(key=lambda x : int(x[0]))
for i in range(N):
    print(f"{people[i][0]} {people[i][1]}")