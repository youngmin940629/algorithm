import sys
input = sys.stdin.readline

N, M  = map(int, input().split())
site = dict()
for _ in range(N):
    key, value = input().split()
    site[key] = value
for _ in range(M):
    key = input().rstrip()
    print(site[key])