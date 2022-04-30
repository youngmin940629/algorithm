for tc in range(int(input())):
    M, N, x, y = map(int, input().split())
    result = -1
    if M > N:
        max_value = [M,x]
        min_value = [N,y]
    else:
        max_value = [N,y]
        min_value = [M,x]
    tmp = min_value[1]
    if tmp % max_value[0] == max_value[1]:
        print(tmp)
    elif max_value[0] == max_value[1] == tmp:
        print(tmp)
    else:
        for i in range(max_value[0]):
            tmp += min_value[0]
            if max_value[0] == max_value[1]:
                if tmp % max_value[0] == 0:
                    result = tmp
                    break
            else:
                if tmp % max_value[0] == max_value[1]:
                    result = tmp
                    break
        print(result)