# K 최대이동 정류장수
# M 충전기가 설치된 정류장 번호갯수
# N 총 정류장수
# 종점 도착불가능할 경우 0출력
# 출발지역 충전기 있음 포함은 x
case = int(input())
cnt = 1
while cnt <= case:
    data = list(map(int, input().split()))
    data_list = list(map(int, input().split()))
    count_list = [0] * (data[1] + 1)
    for count_idx in data_list:
        count_list[count_idx] += 1
    stop_idx = 0
    stop_cnt = 0
    not_charge = 0
    while stop_idx + data[0] < data[1]:
        for idx in range(stop_idx + data[0], stop_idx, -1):
            if count_list[idx] == 1:
                stop_idx = idx
                stop_cnt += 1
                break
            if idx == stop_idx + 1:
                count_list == 0
                stop_cnt = 0
                stop_idx += data[0]
                not_charge = 1
                break
        if not_charge == 1:
            break
    print('#{}' .format(cnt), stop_cnt)
    cnt += 1