N = int(input())
destination = []
for _ in range(N):
    destination.append(list(map(int, input().split())))
destination.sort(key=lambda x : (x[0], x[1]))
for i in range(N):
    print(destination[i][0], destination[i][1])