
def bisearch(arr,s,e,M):
    if s == e:
        ans = s
        return s
    mid = (s + e) // 2
    if M > arr[mid]:
        return bisearch(arr,mid+1,e,M)
    elif M == arr[mid]:
        ans = mid 
        return mid 
    else:
        return bisearch(arr,s,mid-1,M)
    

N,M = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

ans = bisearch(arr,0,len(arr)-1,M)
print(ans+1)


# While 문을 통한 이분검색

# n, m=map(int, input().split())
# a=list(map(int, input().split()))
# a.sort()
# lt=0
# rt=n-1
# while lt<=rt:
#     mid=(lt+rt)//2
#     if a[mid]==m:
#         print(mid+1)
#         break
#     elif a[mid]>m:
#         rt=mid-1
#     else:
#         lt=mid+1











    



    