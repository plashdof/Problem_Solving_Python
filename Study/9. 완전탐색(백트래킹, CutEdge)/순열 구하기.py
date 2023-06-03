
def DFS(n):
    if n == M:
        global cnt 
        cnt+=1
        for i in res:
            print(i,end=" ")
        print()
    else:
        for i in range(1,N+1):
            for j in range(n+1):
                if i == res[j]:
                    break
            else:
                res[n] = i 
                DFS(n+1)

cnt=0
N,M = map(int,input().split())
res = [0]*M 
DFS(0)
print(cnt)






