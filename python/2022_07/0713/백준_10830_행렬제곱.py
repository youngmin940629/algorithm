import sys
input = sys.stdin.readline

N, B = map(int, input().split())
A = list(list(map(int, input().split())) for _ in range(N))
def mul(mat_a, mat_b):
    length = len(mat_a)
    temp = [[0] * length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            for k in range(length):
                temp[i][j] += mat_a[i][k] * mat_b[k][j]
            temp[i][j] %= 1000
    return temp


def matrix_pow(original, n):
    if n == 1:
        return original
    if n % 2 == 0:
        temp = matrix_pow(original, n // 2)
        return mul(temp, temp)
    else:
        temp = matrix_pow(original, n - 1)
        return mul(temp, original)

result = matrix_pow(A, B)
for i in range(N):
    print(' '.join(map(str, result[i])))