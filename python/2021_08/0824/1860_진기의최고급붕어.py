for tc in range(int(input())):
    N, M, K = map(int, input().split())
    people = list(map(int, input().split()))
    max = 0
    bread = 0
    num_people = 0
    result = 'Possible'
    for i in range(len(people)-1, 0, -1):
        for j in range(i):
            if people[j] > people[j+1]:
                people[j], people[j+1] = people[j+1], people[j]
    count_arr = [0] * (people[-1] + 1)
    for peo in people:
        count_arr[peo] += 1
    for idx in range(1, len(count_arr)):
        if count_arr[0] >= 1:
            result = 'Impossible'
            break
        if idx % M == 0:
            bread += K
        if count_arr[idx] != 0:
            num_people += count_arr[idx]
        if num_people > bread:
            result = 'Impossible'
            break
    print('#{} {}'.format(tc+1, result))