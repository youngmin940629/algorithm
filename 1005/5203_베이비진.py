def check_run(arr, idx):
    return arr[idx] >= 1 and arr[idx+1] >= 1 and arr[idx+2] >= 1
def check_triplet(arr, idx):
    return arr[idx] == 3

for tc in range(int(input())):
    card = list(map(int, input().split()))
    player1_cnt = [0] * 10
    player2_cnt = [0] * 10
    result = 0
    break_point = 0
    for idx in range(len(card)):
        if idx % 2:
            player2_cnt[card[idx]] += 1
            for check in range(8):
                if check_run(player2_cnt, check):
                    result = 2
                    break_point = 1
                    break
            for check in range(10):
                if check_triplet(player2_cnt, check):
                    result = 2
                    break_point = 1
                    break
        else:
            player1_cnt[card[idx]] += 1
            for check in range(8):
                if check_run(player1_cnt, check):
                    result = 1
                    break_point = 1
                    break
            for check in range(10):
                if check_triplet(player1_cnt, check):
                    result = 1
                    break_point = 1
                    break
        if break_point == 1:
            break
    print('#{} {}'.format(tc+1, result))