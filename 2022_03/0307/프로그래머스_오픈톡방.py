def solution(record):
    answer = []
    tmp = []
    user = dict()
    for recordItem in record:
        recordItem = recordItem.split(' ')
        if len(recordItem) > 2:
            user[recordItem[1]] = recordItem[2]
            if recordItem[0] == 'Enter':
                tmp.append([0,recordItem[1]])
        else:
            tmp.append([1,recordItem[1]])
    for i in tmp:
        if i[0] == 0:
            answer.append(f"{user[i[1]]}님이 들어왔습니다.")
        else:
            answer.append(f"{user[i[1]]}님이 나갔습니다.")

    return answer

a = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(a))