for tc in range(int(input())):
    N = int(input())
    data = list(input().split())
    result = []
    middle = ((len(data) + 1) // 2)
    for i in range(len(data)):
        if i % 2 == 0:
            result.append(data[i//2])
        elif i % 2 == 1:
            result.append(data[middle + (i//2)])
    print('#{}'.format(tc+1), ' '.join(map(str, result)))