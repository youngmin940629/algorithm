N = int(input())
arr = set()
for _ in range(N):
    arr.add(input())
arr = list(arr)
arr.sort()
arr.sort(key=len)
for word in arr:
    print(word)