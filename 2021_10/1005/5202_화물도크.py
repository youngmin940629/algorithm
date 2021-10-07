for tc in range(int(input())):
    N = int(input())
    time = []
    result = 0
    for _ in range(N):
        time.append(list(map(int, input().split())))
    for i in range(len(time) - 1, 0, -1):
        for j in range(i):
            if time[j][0] > time[j + 1][0]:
                time[j], time[j + 1] = time[j + 1], time[j]
            if time[j][0] == time[j + 1][0] and time[j][1] > time[j + 1][1]:
                time[j], time[j + 1] = time[j + 1], time[j]
    def doke(idx, s):
        global result
        if result < s:
            result = s
        for i in range(idx + 1, len(time)):
            if time[idx][1] <= time[i][0]:
                s += 1
                doke(i,s)
                s -= 1
    for i in range(len(time)):
        doke(i, 1)
    print('#{} {}'.format(tc+1, result))