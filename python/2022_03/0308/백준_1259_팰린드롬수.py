while True:
    num = input()
    if num == '0':
        break
    else:
        for i in range(len(num)):
            if num[i] != num[len(num)-i-1]:
                print('no')
                break
        else:
            print('yes')