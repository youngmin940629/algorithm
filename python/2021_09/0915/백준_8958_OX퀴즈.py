T = int(input())
for _ in range(T):
    data = input()
    result = 0
    score = 0
    for idx in range(len(data)):
        if idx == 0:
            if data[idx] == 'O':
                score = 1
                result += score
            else:
                score = 0
        elif idx > 0:
            if data[idx] == 'O':
                if data[idx-1] == 'O':
                    score += 1
                    result += score
                else:
                    score = 1
                    result += score
            else:
                score = 0
    print(result)