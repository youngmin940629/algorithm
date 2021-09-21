N = int(input())
cnt = 0
for _ in range(N):
    word = input()
    word_dic = dict()
    check_cnt = 0
    for ch in word:
        word_dic[ch] = 0
    for idx in range(len(word)):
        if word_dic[word[idx]] == 1:
            check_cnt = 1
            break
        if idx < (len(word)-1):
            if word[idx] != word[idx+1]:
                word_dic[word[idx]] = 1
    if check_cnt == 0:
        cnt += 1
print(cnt)