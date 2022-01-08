N = int(input())
dice = list(map(int, input().split()))
double_sum = sum(dice)
tri_sum = sum(dice)
for i in range(6):
        for j in range(6):
            if i != j and i + j != 5:
                double_sum = min(double_sum, dice[i] + dice[j])

for i in [0, 5]:
    for j in [1, 4]:
        for k in [2, 3]:
            tri_sum = min(tri_sum, dice[i] + dice[j] + dice[k])

one_side = min(dice)
if N >= 2:
    result = 4 * tri_sum + (4*(N-1) + 4 *(N-2)) * double_sum + (4*((N-2) * (N-1)) + ((N-2)**2))*one_side
else:
    result = sum(dice) - min(dice)
print(result)