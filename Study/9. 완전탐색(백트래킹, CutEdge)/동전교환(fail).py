
def DFS(n,sum,cnt):
    global Min 
    if Min < cnt:
        return 
    if sum > M:
        return 
    if sum == M:
        if Min > cnt: Min = cnt 
    else:
        for i in arr:
            DFS(n+1, sum+i,cnt+1)


Min = 500000
N = int(input())
arr = list(map(int,input().split()))
M = int(input())
DFS(0,0,0)
print(Min)






