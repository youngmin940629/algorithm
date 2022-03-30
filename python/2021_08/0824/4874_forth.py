for tc in range(int(input())):
    data = list(input().split())
    stack = []
    num1, num2 = 0, 0
    for i in range(len(data)):
        if data[i] == '.':
            if len(stack) == 1:
                print('#{} {}'.format(tc+1, stack.pop()))
                break
            else:
                print('#{} {}'.format(tc+1, 'error'))
                break
        if data[i] == '+' or data[i] == '-' or data[i] == '/' or data[i] == '*':
            if len(stack) > 1:
                num1, num2 = stack.pop(), stack.pop()
                if data[i] == '+':
                    stack.append(num2 + num1)
                elif data[i] == '-':
                    stack.append(num2 - num1)
                elif data[i] == '*':
                    stack.append(num2 * num1)
                elif data[i] == '/':
                    stack.append(num2 // num1)
            else:
                print('#{} {}'.format(tc+1, 'error'))
                break
        else:
            stack.append(int(data[i]))