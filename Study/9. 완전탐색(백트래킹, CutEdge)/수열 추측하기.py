import sys

def pascal(arr):
    oldArr = arr[:] 
    while True:
        if len(oldArr) == 1: break 
        newArr = []
        for i in range(len(oldArr)-1):
            newArr.append(oldArr[i] + oldArr[i+1])
        oldArr = newArr[:]
    return oldArr[0]

def DFS(n):
    if n==N:
        if F == pascal(res):
            for i in res:
                print(i,end=" ")
            sys.exit(0)
    else:
        for i in range(1,N+1):
            for j in range(n):
                if res[j] == i:
                    break 
            else:
                res[n] = i 
                DFS(n+1)


N,F = map(int,input().split())
res = [0]*N
DFS(0)
