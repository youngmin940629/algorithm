import sys

N, M = map(int,input().split())
pocketmon = []
pocketmon_dict = dict()

for i in range(N):
    pkmon = sys.stdin.readline().rstrip()
    pocketmon.append(pkmon)
    pocketmon_dict[pkmon] = i
for _ in range(M):
    problem = sys.stdin.readline().rstrip()
    if ord(problem[0]) >= 65 and ord(problem[0]) <=90:
        print(pocketmon_dict[problem]+1)
    else:
        print(pocketmon[int(problem)-1])