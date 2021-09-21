data = list(input())
result = 0
for idx in range(len(data)):
    num = (ord(data[idx]) - ord('A'))
    if 0 <= (num // 3) <= 4:
        result += (num // 3) + 3
    elif 15 <= num <= 18:
        result += 8
    elif 19 <= num <= 21:
        result += 9
    elif 22 <= num:
        result += 10
print(result)