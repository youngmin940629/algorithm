for tc in range(int(input())):
    n = int(input())
    cloth = dict()
    wear = []
    for _ in range(n):
        wear.append(input().split())
        cloth[wear[_][1]] = []
    for i in wear:
        cloth[i[1]].append(i[0])

    result = 1
    for key in cloth:
        result *= (len(cloth[key]) + 1)
    print(result - 1)