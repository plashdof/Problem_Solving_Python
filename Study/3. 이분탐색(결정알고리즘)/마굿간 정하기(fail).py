
def count(mid):
    count = 1
    start = arr[0]
    for i in arr:
        if i - start >= mid:
            start = i 
            count+=1
    if count < C: return False 
    else: return True


N, C = map(int,input().split())
arr = []
for i in range(N):
    temp = int(input())
    arr.append(temp)
arr.sort()
max = arr[N-1] - arr[0]
lt = 1
rt = max  
res = 0
while lt <= rt:
    mid = (lt + rt)//2
    if count(mid): 
        res = mid
        lt = mid+1
    else:
        rt = mid - 1
print(res)
    

# 첫번째 말은 무조건 첫번째마굿간 !!! 이게 중요
# 첫번째 마굿간 기준으로 거리계산
# 적합한 마굿간 찾으면 거기서부터 다시 시작











    



    