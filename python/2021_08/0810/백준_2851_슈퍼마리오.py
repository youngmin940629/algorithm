cnt = 1
mush = []
tmp_score = 0
while cnt <= 10:
    mush.append(int(input()))
    cnt += 1
for idx in range(0,10):
    score = tmp_score
    if score < 100:
        tmp_score += mush[idx]
        if abs(tmp_score - 100) > abs(score - 100):
            tmp_score = score
            break
        if abs(tmp_score - 100) == abs(score - 100):
            score = tmp_score
            break
        else:
            score = tmp_score
print(score)