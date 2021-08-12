for tc in range(int(input())):
    N = int(input())
    num_list = list(map(int, input().split()))
    for i in range(0, len(num_list) - 1):
        if i % 2 == 1:
            min = i
            for j in range(i+1, len(num_list)):
                if num_list[min] > num_list[j]:
                    min = j
            num_list[i], num_list[min] = num_list[min], num_list[i]
        elif i % 2 == 0:
            max = i
            for j in range(i + 1, len(num_list)):
                if num_list[max] < num_list[j]:
                    max = j
            num_list[i], num_list[max] = num_list[max], num_list[i]
    print('#{}'.format(tc + 1), ' '.join(map(str, num_list[0:10])))