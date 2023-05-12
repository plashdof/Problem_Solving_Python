
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