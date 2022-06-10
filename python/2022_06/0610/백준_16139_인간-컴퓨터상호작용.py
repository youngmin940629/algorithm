import sys
input = sys.stdin.readline

S = input().strip()
arr = [[0 for i in range(26)] for _ in range(len(S))]
arr[0][ord(S[0]) - 97] = 1
for i in range(1, len(S)):
    arr[i][ord(S[i]) - 97] = 1
    for j in range(26):
        arr[i][j] += arr[i - 1][j]
for _ in range(int(input())):
    a = input().split()
    if int(a[1]) > 0:
        count = arr[int(a[2])][ord(a[0]) - 97] - arr[int(a[1]) - 1][ord(a[0]) - 97]
    else:
        count = arr[int(a[2])][ord(a[0]) - 97]
    sys.stdout.write(f'{str(count)}\n')