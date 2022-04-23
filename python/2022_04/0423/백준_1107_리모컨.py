n = int(input())
m = int(input())
if m == 0:
    remote = []
else:
    remote = list(map(int, input().split()))
result = abs(n-100)

for num in range(1000001):
    flag = 0
    number = str(num)
    for num_word in number:
        if int(num_word) in remote:
            flag = 1
            break
    if flag == 0:
        tmp = abs(num-n)
        result = min(tmp + len(number), result)
print(result)