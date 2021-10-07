for tc in range(int(input())):
    case = input()
    data = list(input().split())
    arr = [0] * 10
    for num in data:
        if num == 'ZRO':
            arr[0] += 1
        elif num == 'ONE':
            arr[1] += 1
        elif num == 'TWO':
            arr[2] += 1
        elif num == 'THR':
            arr[3] += 1
        elif num == 'FOR':
            arr[4] += 1
        elif num == 'FIV':
            arr[5] += 1
        elif num == 'SIX':
            arr[6] += 1
        elif num == 'SVN':
            arr[7] += 1
        elif num == 'EGT':
            arr[8] += 1
        elif num == 'NIN':
            arr[9] += 1
    print('#{}'.format(tc + 1))
    for num_idx in range(10):
        if num_idx == 0:
            print('ZRO '*arr[num_idx], end = '')
        elif num_idx == 1:
            print('ONE '*arr[num_idx], end = '')
        elif num_idx == 2:
            print('TWO '*arr[num_idx], end = '')
        elif num_idx == 3:
            print('THR '*arr[num_idx], end = '')
        elif num_idx == 4:
            print('FOR '*arr[num_idx], end = '')
        elif num_idx == 5:
            print('FIV '*arr[num_idx], end = '')
        elif num_idx == 6:
            print('SIX '*arr[num_idx], end = '')
        elif num_idx == 7:
            print('SVN '*arr[num_idx], end = '')
        elif num_idx == 8:
            print('EGT '*arr[num_idx], end = '')
        elif num_idx == 9:
            print('NIN '*arr[num_idx], end = '')
    print()