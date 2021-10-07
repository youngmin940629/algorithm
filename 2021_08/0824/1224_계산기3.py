for tc in range(10):
    N = int(input())
    data = input()
    icp = {'*' : 2, '+' : 1, '(' : 3}
    isp = {'*' : 2, '+' : 1, '(' : 0}
    S = []
    postfix = []
    num1, num2 = 0, 0
    for ch in data:
        if ch in icp or ch in isp:
            if not S:
                S.append(ch)
            else:
                if icp[ch] > isp[S[-1]]:
                    S.append(ch)
                else:
                    while S and icp[ch] < isp[S[-1]]:
                        postfix.append(S.pop())
                    S.append(ch)
        elif ch == ')':
            tmp = S.pop()
            while tmp != '(':
                postfix.append(tmp)
                tmp = S.pop()
        else:
            postfix.append(ch)
    for data in postfix:
        if '0' <= data <= '9':
            S.append(int(data))
        elif data == '+':
            num1, num2 = S.pop(), S.pop()
            S.append(num1 + num2)
        elif data == '*':
            num1, num2 = S.pop(), S.pop()
            S.append(num1 * num2)
    print('#{} {}'.format(tc+1, S.pop()))