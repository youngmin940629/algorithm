from collections import deque

N, K = map(int, input().split())
dp = [0xffffff] * (100001)
st = N
q = deque()
q.append((N))
dp[N] = 0
while q:
    st = q.popleft()
    if st == K:
        break
    if st - 1 >= 0 and dp[st] + 1 < dp[st-1]:
        dp[st-1] = dp[st] + 1
        q.append((st-1))
    if st + 1 <= 100000 and dp[st] + 1 < dp[st+1]:
        dp[st+1] = dp[st] + 1
        q.append((st+1))
    if st * 2 <= 100000 and dp[st] < dp[st*2]:
        dp[st*2] = dp[st]
        q.append((st*2))
print(dp[K])