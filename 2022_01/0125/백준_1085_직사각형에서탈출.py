x, y, w, h = list(map(int, input().split()))
result = min(x,y,abs(w-x),abs(h-y))
print(result)