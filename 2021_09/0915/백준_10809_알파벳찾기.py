data = [-1] * 26
word = input()
for idx in range(len(word)):
    if ord('a') <= ord(word[idx]) <= ord('z'):
        if data[ord(word[idx]) - ord('a')] == -1:
            data[ord(word[idx]) - ord('a')] = idx
print(' '.join(map(str,data)))