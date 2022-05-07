N, M = map(int,input().split())
arr = list(map(int, input().split()))
arr.sort()

def permutation(n, tmp_arr):
    if n == M:
        print(' '.join(map(str , tmp_arr)))
    else:
        for num in arr:
            if num in tmp_arr:
                continue
            else:
                tmp = tmp_arr[:]
                tmp.append(num)
                permutation(n+1, tmp)

permutation(0,[])