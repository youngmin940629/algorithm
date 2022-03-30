N, M = map(int, input().split())
trees = list(map(int ,input().split()))    
st, end = 1, max(trees)

while st <= end:
    mid = ((st+end)//2)
    total = 0
    for i in range(len(trees)):
        if trees[i] > mid:
            total += (trees[i]-mid)
    if total > M:
        st = mid + 1
    elif total < M:
        end = mid-1
    elif total == M:
        break
print((st+end)//2)