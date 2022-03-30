for tc in range(int(input())):
    money = int(input())
    result = [0] * 8
    if money >= 50000:
        result[0] = money//50000
        money %= 50000
    if money >= 10000:
        result[1] = money//10000
        money %= 10000
    if money >= 5000:
        result[2] = money//5000
        money %= 5000
    if money >= 1000:
        result[3] = money//1000
        money %= 1000
    if money >= 500:
        result[4] = money//500
        money %= 500
    if money >= 100:
        result[5] = money//100
        money %= 100
    if money >= 50:
        result[6] = money//50
        money %= 50
    if money >= 10:
        result[7] = money//10
        money %= 10
    print('#{}\n{}'.format(tc+1, ' '.join(map(str, result))))