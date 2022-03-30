N = int(input())
tree_arr = []
for _ in range(N):
    tree_arr.append(list(map(int, input().split())))
total = 0
for i in range(N):
    total += tree_arr[i][2]

def select_tree(n, m, arr_tree):
    global total, result
    if result:
        return
    else:
        if len(arr_tree) == n:
            fence_num = total
            for i in arr_tree:
                fence_num -= i[2]
            if check(arr_tree, fence_num):
                result = n
                return
        else:
            for i in range(m, N):
                tmp = arr_tree[:]
                tmp.append(tree_arr[i])
                select_tree(n, i+1, tmp)

def check(arr, num):
    arr.sort(key=lambda x : x[0])
    x1, x2 = arr[0][0], arr[-1][0]
    arr.sort(key=lambda x : x[1])
    y1, y2 = arr[0][1], arr[-1][1]
    fence = 2*(abs(x1-x2) + abs(y1-y2))
    if fence > num:
        return
    return True

number = N-1
result = 0
while number > 0:
    select_tree(number, 0, [])
    if result:
        break
    else:
        number -= 1
print(N-result)