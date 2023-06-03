
def DFS(n,start):
    if n==M:
        global cnt 
        cnt+=1
        for i in res:
            print(i,end=" ")
        print()
    else:
        for i in range(start,N+1):
            res[n] = i 
            DFS(n+1,i+1)
                

cnt = 0
N,M = map(int,input().split())
res = [0]*M 
DFS(0,1)
print(cnt)