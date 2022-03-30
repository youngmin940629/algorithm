import sys

for data in sys.stdin:
    A, B = map(int, data.split())
    print(A+B)