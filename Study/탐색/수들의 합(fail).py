
# 처음 permutations 로 모든 경우의 수 따졌지만, timelimit 발생
# 모든 경우의수 구할 필요 없었음
# Sliding Window 활용!!

N, M = map(int,input().split())
arr = list(map(int,input().split()))
ws = 0
we = 1
count = 0
total = arr[0]
while True:
    if total < M:
        if we < N:
            total+=arr[we]
            we+=1
        else:
            # total 이 M보다 작은데, we 가 배열 끝에 가있으면, 
            # 더이상 부분합이 M 인 배열이 없다는뜻
            break 
    elif total == M:
        count+=1
        total-=arr[ws]
        ws+=1
    else:
        total-=arr[ws]
        ws+=1

print(count)










    



    