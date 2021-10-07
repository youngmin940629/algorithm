A, B = map(str,input().split())
data = [[] for _ in range(2)]
A_new = B_new = 0
for idx in range(2, -1, -1):
    data[0].append(A[idx])
    data[1].append(B[idx])
for i in range(3):
    A_new += (10 ** i) * int(data[0][2-i])
    B_new += (10 ** i) * int(data[1][2-i])
if A_new > B_new:
    print(A_new)
else:
    print(B_new)