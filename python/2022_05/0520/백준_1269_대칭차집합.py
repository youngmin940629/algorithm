A, B = map(int, input().split())
arr_A = set(map(int,input().split()))
arr_B = set(map(int, input().split()))
print(len(arr_A-arr_B)+len(arr_B-arr_A))