T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print('Case #{}: {} + {} = {}'.format(_+1, A, B, A+B))