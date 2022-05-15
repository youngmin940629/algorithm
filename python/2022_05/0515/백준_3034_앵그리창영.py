N, W, H = map(int, input().split())
for _ in range(N):
    n = int(input())
    if n ** 2 <= W ** 2 + H ** 2:
        print("DA")
    else:
        print("NE")