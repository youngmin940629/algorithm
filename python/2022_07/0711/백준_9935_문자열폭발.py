word = input()
explosion = input()
lastword = explosion[-1]

stack = []
length = len(explosion)

for i in range(len(word)):
    stack.append(word[i])
    if stack[-1] == lastword and len(stack) >= length:
        if ''.join(stack[-length:]) == explosion:
            for j in range(length):
                stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')