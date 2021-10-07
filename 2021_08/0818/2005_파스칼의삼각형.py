def pascal(N):
    result = [1]
    if N == 1:
        return result
    elif N == 2:
        result.append(1)
        return result
    else:
        for i in range(1, N - 1):
            result.append(pascal(N-1)[i-1] + pascal(N-1)[i])
            if i == (N - 2):
                result.append(1)
    return result

for tc in range(int(input())):
    print('#{}'.format(tc+1))
    num = int(input())
    for number in range(1, num + 1):
        print(' '.join(map(str, pascal(number))))