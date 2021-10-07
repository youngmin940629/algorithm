def order(n):
    global result, N
    if n >= N:
        return
    if left[n] > 0:
        order(left[n])
    if right[n] > 0:
        order(right[n])
    if node[n] == '+':
        node[n] = node[left[n]] + node[right[n]]
    elif node[n] == '-':
        node[n] = node[left[n]] - node[right[n]]
    elif node[n] == '*':
        node[n] = node[left[n]] * node[right[n]]
    elif node[n] == '/':
        node[n] = node[left[n]] / node[right[n]]

for tc in range(10):
    N = int(input())
    left = [0] * 1001
    right = [0] * 1001
    node = [0]
    result = 0
    for _ in range(1, N+1):
        data = list(map(str, input().split()))
        if len(data) == 4:
            left[int(data[0])] = int(data[2])
            right[int(data[0])] = int(data[3])
            node.append(data[1])
        else:
            node.append(int(data[1]))
    order(1)
    print("#{} {}".format(tc+1, int(node[1])))