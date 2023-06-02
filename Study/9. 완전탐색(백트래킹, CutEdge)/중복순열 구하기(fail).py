def DFS(n):
    global cnt 
    if n == M:
        for i in res:
            print(i,end=" ")
        cnt+=1
        print()
    else:
        for i in range(1,N+1):
            res[n]=i 
            DFS(n+1)


N,M = map(int,input().split())
res = [0]*M 
cnt = 0
DFS(0)
print(cnt)


# 다중 상태트리 문제

# 이진에서는 두가지만 재귀해주면 되었지만,
# 다중상태트리에서는 for문으로 여러번 재귀