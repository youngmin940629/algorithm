for tc in range(int(input())):
    N = int(input())
    data = list(map(int, input().split()))
    stack = []
    result = 0
    for case in data:
        if case == 0:
            stack.pop()
        else:
            stack.append(case)
    for rst in stack:
        result += rst
    print('#{}'.format(tc+1), result)