
N, K = map(int, input().split())
arr = []

for i in range(1,N+1):
    if N % i == 0:
        arr.append(i)

if len(arr) < K :
    print(-1)
else:
    print(arr[K-1])



# 배열 안쓰고, 그냥 count 변수로 카운팅 해도 됨!
# n, k=map(int, input().split())
# cnt=0
# for i in range(1, n+1):
#     if n%i==0:
#         cnt+=1
#     if cnt==k:
#         print(i)
#         break
# else:
#     print(-1)