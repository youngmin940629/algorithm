import sys
input = sys.stdin.readline
import heapq

for _ in range(int(input())):
    T = int(input())
    min_heap = []
    max_heap = []
    for _ in range(T):
        action = input().split()
        if action[0] == 'I':
            number = int(action[1])
            heapq.heappush(min_heap, number)
            heapq.heappush(max_heap, ((-1) * number, number))
        elif action[0] == 'D':
            if not min_heap:
                pass
            elif action[1] == '1':
                value = heapq.heappop(max_heap)[1]
                min_heap.remove(value)
            elif action[1] == '-1':
                value = heapq.heappop(min_heap)
                max_heap.remove(((-1)*value, value))
    
    if min_heap:
        print(heapq.heappop(max_heap)[1], heapq.heappop(min_heap))
    else:
        print('EMPTY')