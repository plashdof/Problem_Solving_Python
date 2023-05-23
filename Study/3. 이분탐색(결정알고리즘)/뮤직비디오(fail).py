# 답의 값 범위 정해져 있다!!

def counting(arr,mid):
    temp = 0
    count = 0
    for i in arr:
        temp+=i
        if temp > mid:
            temp = i 
            count+=1
        elif temp == mid:
            temp = 0
            count+=1 
    if temp != 0 : count+=1
    return count 
            

N, M = map(int, input().split())
arr = list(map(int,input().split()))
maX = sum(arr)

# 가장 큰곡 한개를 담을수있는 사이즈가 최솟값이므로, 
# 가장 긴 노래 길이가 최솟값
miN = max(arr)

lt = miN
rt = maX
res = 0

while lt <= rt:
    mid = (lt + rt)//2
    temp = counting(arr,mid)
    # temp < M 이더라도, 답이 될수 있는 값인것이다!!
    if temp <= M:
        res = mid 
        rt = mid - 1
    else:
        lt = mid + 1
print(res)




# def Count(capacity):
#     cnt=1
#     sum=0
#     for x in Music:
#         if sum+x>capacity:
#             cnt+=1
#             sum=x
#         else:
#             sum+=x
#     return cnt

# n, m=map(int, input().split())
# Music=list(map(int, input().split()))
# maxx=max(Music)
# lt=1
# rt=sum(Music)
# res=0
# while lt<=rt:
#     mid=(lt+rt)//2
#     if mid>=maxx and Count(mid)<=m:
#         res=mid
#         rt=mid-1
#     else:
#         lt=mid+1
# print(res)








    



    