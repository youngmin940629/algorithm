for tc in range(int(input())):
    N = int(input())
    data = list(map(int, input().split()))
    result = 0
    max = data[-1]
    for i in range(N-1, -1, -1):
        if max > data[i]:
            result += max - data[i]
        else:
            max = data[i]
    print('#{} {}'.format(tc+1, result))