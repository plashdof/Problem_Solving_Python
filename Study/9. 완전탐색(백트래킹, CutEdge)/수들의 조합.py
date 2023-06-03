
def DFS(n,start):
    if n==K:
        global cnt 
        temp = sum(res)
        if temp % M == 0:
            cnt+=1
    else:
        for i in range(start,N):
            res[n] = arr[i]
            DFS(n+1, i+1)

cnt=0
N,K = map(int,input().split())
arr = list(map(int,input().split()))
M = int(input())
res=[0]*K
DFS(0,0)
print(cnt)