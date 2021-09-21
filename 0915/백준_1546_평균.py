N = int(input())
score = list(map(int, input().split()))
M = max(score)
total = 0
for idx in range(N):
    total += score[idx]
print((total/(M*len(score)))*100)