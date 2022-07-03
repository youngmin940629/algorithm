S1, S2, S3 = map(int, input().split())
arr = [0] * (S1+S2+S3+1)
for i in range(1,S1+1):
    for j in range(1,S2+1):
        for k in range(1,S3+1):
            arr[i+j+k] += 1
print(arr.index(max(arr)))