
def DFS(n):
    if n==N:
        global cnt 
        cnt+=1
    else:
        for i in range(1,N+1):
            if i != n:
                if arr[n][i] == 1:
                    arr[n][i] = 2
                    DFS(i)

cnt =0
N,M = map(int,input().split())
arr=[[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    arr[a][b] = 1
print(arr)
DFS(1)
print(cnt)