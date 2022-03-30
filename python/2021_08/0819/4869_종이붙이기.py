def paper(length):
    if length == 10:
        return 1
    elif length == 20:
        return 3
    else:
        return paper(length-10) + paper(length-20) * 2
for tc in range(int(input())):
    N = int(input())
    print('#{} {}'.format(tc+1, paper(N)))