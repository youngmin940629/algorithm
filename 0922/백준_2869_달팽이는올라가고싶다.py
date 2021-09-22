A, B, V = map(int,input().split())
def snail(height, day, night):
    if day <= night:
        return '달팽이가 못올라가요..'
    elif (height - day) % (day - night) == 0:
        return ((height - day) // (day - night)) + 1
    elif (height - day) % (day - night) != 0:
        return ((height - day) // (day - night)) + 2

print(snail(V, A, B))