while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    result = ''
    if A > B:
        if A % B == 0:
            result = 'multiple'
        else:
            result = 'neither'
    if A < B:
        if B % A == 0:
            result = 'factor'
        else:
            result = 'neither'
    print(result)