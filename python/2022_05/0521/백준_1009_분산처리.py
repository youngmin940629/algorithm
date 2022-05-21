for tc in range(int(input())):
    a, b = map(int, input().split())
    num = a % 10
    rule = dict()
    rule = {2:[2,4,8,6], 3:[3,9,7,1], 4:[4,6], 7:[7,9,3,1],8:[8,4,2,6],9:[9,1]}
    if num == 1 or num == 5 or num == 6:
        print(num)
    elif num == 0:
        print(10)
    elif num == 2 or num == 3 or num == 7 or num == 8:
        print(rule[num][(b-1)%4])
    else:
        print(rule[num][(b-1)%2])