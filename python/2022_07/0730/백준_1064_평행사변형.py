X1, Y1, X2, Y2, X3, Y3 = map(int,input().split())

result = 0
if X1 == X2 == X3 or Y1 == Y2 == Y3 :
    result = -1
elif Y1-Y2 != 0 and Y1-Y3 != 0 and Y2-Y3 != 0 \
    and (X1-X2)/(Y1-Y2) == (X2-X3)/(Y2-Y3) == (X1-X3)/(Y1-Y3):
    result = -1
else :
    dAB = ((X1-X2)**2 + (Y1-Y2)**2) ** (1/2)
    dBC = ((X2-X3)**2 + (Y2-Y3)**2) ** (1/2)
    dCA = ((X3-X1)**2 + (Y3-Y1)**2) ** (1/2)

    result = (max(dAB, dBC, dCA) - min(dAB, dBC, dCA)) * 2

print(result)