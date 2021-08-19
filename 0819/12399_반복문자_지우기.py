for tc in range(int(input())):
    st = input()
    result = []
    for word in st:
        if result == []:
            result.append(word)
        elif result[-1] != word:
            result.append(word)
        else:
            result.pop()
    while True:
        for idx in range(len(result) - 1):
            if result[idx] == result[idx+1]:
                result[idx], result[idx+1] = [], []
                break
        else:
            break
    print('#{} {}'.format(tc+1, len(result)))