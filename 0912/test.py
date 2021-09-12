import math
hole = [[0,127], [127,127], [254,127], [0,0], [127,0], [254,0]]

ball_1 = [127,63.5]
ball_2 = [62, 97]
distance_hole = 1000
for hole_idx in range(6):
    tmp_distance = (((hole[hole_idx][0] - ball_2[0]) ** 2) + ((hole[hole_idx][1] - ball_2[1]) ** 2)) ** (1/2) + (((ball_1[0] - ball_2[0]) ** 2) + ((ball_1[1] - ball_2[1]) ** 2)) ** (1/2)
    if distance_hole > tmp_distance:
        distance_hole = tmp_distance
        target_hole_idx = hole_idx
target_hole = hole[target_hole_idx]
print(target_hole)
for i in range(2):
    if i == 0:
        x = target_hole[i] - ball_2[i]
    elif i == 1:
        y = target_hole[i] - ball_2[i]

angle = math.atan(y/x)
for j in range(2):
    if j == 0:
        target_x = ball_2[j] - 2 * math.cos(angle)
    elif j == 1:
        target_y = ball_2[j] - 2 * math.sin(angle)

target_loaction = [target_x,target_y]
print(target_loaction)
target_angle = math.atan((target_x - ball_1[0]) / (target_y - ball_1[1]))
print(target_angle)
print(math.degrees(target_angle))
