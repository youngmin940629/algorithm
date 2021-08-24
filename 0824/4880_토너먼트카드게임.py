for tc in range(int(input())):
    N = int(input())
    data = [0] + list(map(int, input().split()))
    def win(a,b):
        if data[a] == data[b]:
            if data[a] <= data[b]:
                return a
            else:
                return b
        elif data[a] == 1:
            if data[b] == 2:
                return b
            elif data[b] == 3:
                return a
        elif data[a] == 2:
            if data[b] == 1:
                return a
            elif data[b] == 3:
                return b
        elif data[a] == 3:
            if data[b] == 1:
                return b
            elif data[b] == 2:
                return a
    def div(start, end):
        if start == end:
            return start
        st_num = div(start, (start+end) // 2)
        end_num = div((start+end)//2 +1, end)
        return win(st_num,end_num)
    result = div(1,N)
    print('#{} {}'.format(tc+1, result))