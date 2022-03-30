L = int(input())
word = input()
total = 0
for index in range(len(word)):
    total += ((ord(word[index]) - 96) * 31 **(index))
result = total % 1234567891
print(result)