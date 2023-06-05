
# 내풀이
# 결과 : Success

def DFS(n,sum):
    if n==K:
        if sum > 0: ch[sum]=1
        return
    else:
        DFS(n+1,sum-arr[n])
        DFS(n+1,sum+arr[n])
        DFS(n+1,sum)


K = int(input())
arr = list(map(int,input().split()))
S = sum(arr)
ch = [0]*(S+1)
cnt=0
DFS(0,0)
for i in range(1,S+1):
    if ch[i]==0:
        cnt+=1
print(cnt)