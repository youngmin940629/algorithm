for tc in range(10):
    N = int(input())
    data = input()
    icp = {'*' : 2, '+' : 1}
    result = 0
    postfix = []
    S = []
    cal_s = []
    for ch in data:
        if ch in icp:
            if not S:
                S.append(ch)
            else:
                if icp[ch] > icp[S[-1]]:
                    S.append(ch)
                else:
                    while S and icp[ch] < icp[S[-1]]:
                        postfix.append(S.pop())
                    S.append(ch)
        else:
            postfix.append(ch)
    while S:
        postfix.append(S.pop())
    for val in postfix:
        if '0' <= val <= '9':
            cal_s.append(int(val))
        elif val == '+':
            result = cal_s.pop() + cal_s.pop()
            cal_s.append(result)
        elif val == '*':
            result = cal_s.pop() * cal_s.pop()
            cal_s.append(result)
    print('#{} {}'.format(tc+1, result))
