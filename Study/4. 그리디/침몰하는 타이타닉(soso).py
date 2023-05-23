
N,M = map(int, input().split())
arr = list(map(int,input().split()))
arr.sort(reverse=True)
arrState = [0]*N 
count = 0
state = False
for i in range(N):
    if arrState[i] == 1:
        continue 

    for j in range(i+1,N):
        if arrState[j] == 1:
            continue

        if arr[i]+arr[j] <= M:
            arrState[i] = 1
            arrState[j] = 1
            count+=1
            state = True 
            break 

    if not state:
         arrState[i] = 1
         count+=1
    else:
        state = False 

print(count)


# 내림차순으로 나열
# 가장 높은몸무게 순으로, 무조건 2명 짝으로 빼기
# 짝은 가장 높은몸무게순으로 설정
    



# 짝 고를때, 가장 높은몸무게순으로 설정할 필요는 없었음!!
# 그냥 배열 양쪽에서 pop 해 가며, 담아가면 됨

# from collections import deque    

# n, limit=map(int, input().split())
# p=list(map(int, input().split()))
# p.sort()
# p=deque(p)
# cnt=0
# while p:
#     if len(p)==1:
#         cnt+=1
#         break
#     if p[0]+p[-1]>limit:
#         p.pop()
#         cnt+=1
#     else:
#         p.popleft()
#         p.pop()
#         cnt+=1
# print(cnt)

# 배열에서 맨앞원소 pop 하게되면, 매우 비효율적임.
# 따라서, deque로 변환