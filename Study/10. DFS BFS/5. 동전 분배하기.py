# 내풀이
# 결과 : success
# 동전종류과 크기같은 배열 res 만들어서, 해당 동전을 누가 가지는지 'A', 'B', 'C' 로 표시

def DFS(n):
    global Min 
    if n==N :
        Asum=0
        Bsum=0
        Csum=0
        for i,data in enumerate(res):
            if data=='A':
                Asum+=arr[i]
            elif data=='B':
                Bsum+=arr[i]
            else:
                Csum+=arr[i]
        
        if Asum== Bsum or Asum==Csum or Bsum==Csum:
            return 
        temp = max(Asum,Bsum,Csum) - min(Asum,Bsum,Csum)
        if temp < Min:
            Min = temp 
        return 
    else:
        res[n]='A' 
        DFS(n+1)
        res[n]='B'
        DFS(n+1)
        res[n]='C'
        DFS(n+1)

Min=24700000
N = int(input())
arr=[]
for i in range(N):
    t = int(input())
    arr.append(t)
res = [''] * N 
DFS(0)
print(Min)