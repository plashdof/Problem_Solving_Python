# 내풀이 
# 결과 : Success
# 세부조건이 많았다. 그리고 indexError 가 많아서, 주의해야겠다

def DFS(x,y):
    global cnt
    if x==-1 or y==-1 or x==N or y==N:
        return 
    if x==ex and y==ey:
        cnt+=1
        return 
    else:
        if ch[x][y]==0:
            ch[x][y] = 1
            if x < N-1 and arr[x+1][y] > arr[x][y]: DFS(x+1,y)
            if y < N-1 and arr[x][y+1] > arr[x][y]: DFS(x,y+1)
            if x > 0 and arr[x-1][y] > arr[x][y]: DFS(x-1,y)
            if y > 0 and arr[x][y-1] > arr[x][y]: DFS(x,y-1)
            ch[x][y]=0



N = int(input())
arr=[]
start = 2147000000
end = -2147000000
sx = sy = 0
ex = ey = 0
for i in range(N):
    tt = list(map(int,input().split()))
    a = min(tt)
    
    b = max(tt)
    if start > a : 
        start = a
        sx = i
        sy = tt.index(a) 
    if end < b : 
        end = b 
        ex = i
        ey = tt.index(b)
    arr.append(tt)
ch = [[0] * N for _ in range(N)]
cnt = 0
DFS(sx,sy)
print(cnt)