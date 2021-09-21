word = input()
cnt_arr = [0] * 26
for ch in word:
    if 0 <= ord(ch) - ord('a') <= 25:
        cnt_arr[ord(ch) - ord('a')] += 1
    elif 0 <= ord(ch) - ord('A') <= 25:
        cnt_arr[ord(ch) - ord('A')] += 1
max_num = max(cnt_arr)
cnt = 0
max_idx = 0
for idx in range(26):
    if cnt_arr[idx] == max_num:
        cnt += 1
        max_idx = idx
if cnt > 1:
    print('?')
else:
    print(chr(max_idx + ord('A')))