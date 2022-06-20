a = list(input())
stack=[]
result=''
for s in a:
    if ord('A') <= ord(s) <= ord('Z'):
        result+=s
    else:
        if s == '(':
            stack.append(s)
        elif s == '*' or s == '/':
            while stack and (stack[-1] == '*' or stack[-1] =='/'):
                result += stack.pop()
            stack.append(s)
        elif s == '+' or s == '-':
            while stack and stack[-1] != '(':
                result+= stack.pop()
            stack.append(s)
        elif s == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()
while stack :
    result+=stack.pop()
print(result)
