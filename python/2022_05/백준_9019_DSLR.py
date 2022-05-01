from collections import deque

# # 메모리 초과 ..
# for tc in range(int(input())):
#     A, B = map(int, input().split())
#     d = ['D', 'S', 'L', 'R']
#     q = deque()
#     q.append((A, ''))
#     result = ''
#     while q:
#         num, path = q.popleft()
#         if num == B:
#             result = path
#             break
#         else:
#             for next in d:
#                 if next == 'D':
#                     if num * 2 > 9999:
#                         q.append(((num*2)%10000,path+next))
#                     else:
#                         q.append((num*2, path+next))
#                 elif next == 'S':
#                     if num - 1 == 0:
#                         q.append((9999, path+next))
#                     else:
#                         q.append((num-1, path+next))
#                 elif next == 'L':
#                     tmp = num / 1000
#                     x, y = int(tmp), (tmp-int(tmp))*1000
#                     q.append((int(x+y*10), path+next))
#                 elif next == 'R':
#                     tmp = num / 10
#                     x, y = int(tmp) , tmp - int(tmp)
#                     q.append((int(x+y*1000) , path+next))
#     print(result)


for _ in range(int(input())):
    A,B = map(int,input().split())
    q = deque()
    q.append((A,""))
    visit = [False] * 10000
    result = ''
    while q:
        num, path = q.popleft()
        visit[num] = True
        if num == B:
            result = path
            break
        tmp = (2*num)%10000
        if not visit[tmp]:
            q.append((tmp,path+"D"))
            visit[tmp] = True
        tmp = (num-1)%10000
        if not visit[tmp]:
            q.append((tmp,path+"S"))
            visit[tmp] = True
        tmp = (10*num+(num//1000))%10000
        if not visit[tmp]:
            q.append((tmp,path+"L"))
            visit[tmp] = True
        tmp = (num//10+(num%10)*1000)%10000
        if not visit[tmp]:
            q.append((tmp,path+"R"))
            visit[tmp] = True
    print(result)