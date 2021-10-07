def bus(station, cnt):
    global result
    if station >= data[0]:
        if result > cnt:
            result = cnt
            return
    elif result <= cnt:
        return
    else:
        for idx in range(1, charge[station]+1):
            cnt += 1
            bus(station+idx, cnt)
            cnt -= 1



for tc in range(int(input())):
    data = list(map(int, input().split()))
    charge = [0] * data[0]
    result = data[0]
    for idx in range(1, len(data)):
        charge[idx] = data[idx]
    bus(1, 0)
    print('#{} {}'.format(tc+1, result-1))