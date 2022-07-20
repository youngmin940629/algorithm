A, B, N = map(int, input().split())
quotient, remainder = A // B, A % B * 10
count = 0
while True:
    decimal = remainder // B

    count += 1
    if count == N:
        break
    else:
        remainder = (remainder % B) * 10
print(decimal)