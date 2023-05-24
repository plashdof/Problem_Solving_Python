from collections import deque

N,M = map(int,input().split())
arr = list(map(int,input().split()))
deq = deque(arr)
indexDeq = deque(list(range(N)))

cnt = 0
while True:
    temp = deq.popleft()
    indexTemp = indexDeq.popleft()
    max = temp 
    for i in deq:
        if max < i:
            max = i 
            deq.append(temp)
            indexDeq.append(indexTemp)
            break 
    if max == temp:
        cnt+=1
        if indexTemp == M:
            print(cnt)
            break
    

# deque 두개만드는게 아니라, index와 값을 튜플하나로 지정해서, 하나의 deque로 해결

# Q=[(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
# Q=deque(Q)
# cnt=0
# while True:
#     cur=Q.popleft()
#     if any(cur[1]<x[1] for x in Q):
#         Q.append(cur)
#     else:
#         cnt+=1
#         if cur[0]==m:
#             print(cnt)
#             break




