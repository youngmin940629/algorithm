word = list(input())
idx = 0
result = []
while idx <= (len(word) - 1):
    if word[idx] == 'c':
        if idx < (len(word)-1) and word[idx+1] == '=':
            result.append(0)
            idx += 2
        elif idx < (len(word)-1) and word[idx+1] == '-':
            result.append(0)
            idx += 2
        else:
            result.append('c')
            idx += 1
    elif word[idx] == 'd':
        if idx < (len(word) - 2) and word[idx + 1] == 'z' and word[idx+2] == '=':
            result.append(0)
            idx += 3
        elif idx < (len(word) - 1) and word[idx + 1] == '-':
            result.append(0)
            idx += 2
        else:
            result.append('d')
            idx += 1
    elif word[idx] == 'l':
        if idx < (len(word)-1) and word[idx+1] == 'j':
            result.append(0)
            idx += 2
        else:
            result.append('l')
            idx += 1
    elif word[idx] == 'n':
        if idx < (len(word)-1) and word[idx+1] == 'j':
            result.append(0)
            idx += 2
        else:
            result.append('n')
            idx += 1
    elif word[idx] == 's':
        if idx < (len(word)-1) and word[idx+1] == '=':
            result.append(0)
            idx += 2
        else:
            result.append('s')
            idx += 1
    elif word[idx] == 'z':
        if idx < (len(word)-1) and word[idx+1] == '=':
            result.append(0)
            idx += 2
        else:
            result.append('z')
            idx += 1
    else:
        result.append(word[idx])
        idx += 1
print(len(result))