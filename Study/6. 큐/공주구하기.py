from collections import deque

N, K = map(int,input().split())
deq = deque()
for i in range(1,N+1):
    deq.append(i)

# 그냥 리스트 만들고 deq로 처리가 더 깔끔
# arr = list(range(1,N+1))
# deq = deque(arr)

cnt = K 
while len(deq) > 1:
    if cnt == 1:
        deq.popleft()
        cnt = K
    else:
        deq.append(deq.popleft())
        cnt-=1
print(deq[0])


# cnt 변수를 설정하지 않고 for문으로 K번 돌리기

# while dq:
#     for _ in range(k-1):
#         cur=dq.popleft()
#         dq.append(cur)
#     dq.popleft()
#     if len(dq)==1:
#         print(dq[0])
#         dq.popleft()
