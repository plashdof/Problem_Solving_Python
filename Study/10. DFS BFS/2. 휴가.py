# 내풀이
# 결과 : Success
# 순열임. 선택하거나, 선택안하거나

def DFS(n,pay):
    global max 
    if n == N:
        if max < pay : max = pay 
        return 
    else:
        if n+arr[n][0] > N or n+1 > N:
            if max < pay : max = pay 
            return 
        DFS(n+arr[n][0],pay+arr[n][1])
        DFS(n+1, pay)


max = 0
N = int(input())
arr=[]
for i in range(N):
    day,pay = map(int,input().split())
    arr.append((day,pay))
DFS(0,0)
print(max)