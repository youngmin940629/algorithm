import sys
input = sys.stdin.readline

for _ in range(int(input())):
    A, B = map(int, input().split())
    tmp_a,tmp_b=A,B
    while A%B!=0:
        A,B=B,A%B 
        
    print(tmp_a*tmp_b//B)