T = int(input())
for tc in range(T):
    data = list(input().split())
    result = []
    for word in data[1]:
        result.append(int(data[0])*word)
    print(''.join(map(str, result)))