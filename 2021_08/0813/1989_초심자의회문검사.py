for tc in range(int(input())):
    word = input()
    length = 0
    result = 0
    for idx in word:
        length += 1
    for idx in range(length // 2):
        if word[idx] == word[length - 1 - idx]:
            result = 1
        else:
            result = 0
            break
    print('#{}'.format(tc + 1), result)