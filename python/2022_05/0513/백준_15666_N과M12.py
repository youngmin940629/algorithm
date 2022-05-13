N, M = map(int, input().split())
arr = list(set(map(int, input().split())))
arr.sort()

nums=[]

def bfs(n):
    if n == M:
        print(" ".join(map(str, nums)))
        return
    for i in range(len(arr)):
        if n == 0 or nums[-1] <= arr[i]:
            nums.append(arr[i])
            bfs(n+1)
            nums.pop()

bfs(0)
