for tc in range(int(input())):
    data = input()
    stack = []
    result = 1
    for word in data:
        if word == '(' or word == '{':
            stack.append(word)
        elif word == ')':
            if stack == [] or stack.pop() != '(':
                result = 0
                break
        elif word == '}':
            if stack == [] or stack.pop() != '{':
                result = 0
                break
    if stack != []:
        result = 0
    print('#{} {}'.format(tc+1, result))