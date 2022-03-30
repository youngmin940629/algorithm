while True:
    string = input()
    if string == '.':
        break
    else:
        stack = []
        flag = 0
        for word in string:
            if word == '(' or word == '[':
                stack.append(word)
            elif word == ')':
                if stack:
                    check = stack.pop()
                    if check != '(':
                        flag = 1
                        break
                else:
                    flag = 1
                    break
            elif word == ']':
                if stack:
                    check = stack.pop()
                    if check != '[':
                        flag = 1
                        break
                else:
                    flag = 1
                    break
        else:
            if len(stack) > 0:
                flag = 1
        if flag == 1:
            print('no')
        else:
            print('yes')
