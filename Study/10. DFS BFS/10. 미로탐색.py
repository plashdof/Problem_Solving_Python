
# 내 풀이
# 결과 : Success

def DFS(x,y):
    global cnt
    if x==-1 or y==-1 or x==7 or y==7:
        return 
    if arr[x][y]==1:
        return 
    if x==6 and y==6:
        cnt+=1
        return 
    else:
        arr[x][y] = 1
        DFS(x+1,y)
        DFS(x,y+1)
        DFS(x-1,y)
        DFS(x,y-1)
        arr[x][y] = 0

cnt = 0
arr=[]
for i in range(7):
    tt = list(map(int,input().split()))
    arr.append(tt)
DFS(0,0)
print(cnt)