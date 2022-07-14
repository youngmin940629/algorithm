n = int(input())
result = []
count = 0

for _ in range(n):
    word = input()
    if word not in result:
        count += 1
        for i in range(len(word)):
            result.append(word[i:] + word[:i])
print(count)