def solution(n,left,right):
    result = []
    for i in range(left, right+1):
        i = i + 1
        if i % n == 0:
            y = n
            x = i // n
        else:
            y = i % n
            x = (i // n) + 1
        if x < y:
            result.append(y)
        else:
            result.append(x)

    return result

print(solution(4,7,14))