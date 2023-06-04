
# 내풀이
# 결과 : Fail. 자꾸 35나 40나옴

def DFS(n,Ssum,Tsum):
    global max 
    for i in range(n,N):
        if ch[i]==0:
            ch[i] = 1
            if Tsum+arr[i][1] > M:
                if max < Ssum : max = Ssum 
                return 
            DFS(n+1,Ssum+arr[i][0],Tsum+arr[i][1])
            ch[i] = 0


max = 0
N,M = map(int,input().split())
arr=[]
for i in range(N):  
    s,t = map(int,input().split())
    arr.append((s,t))
ch = [0]*N 
DFS(0,0,0)
print(max)


# 수정풀이

# 뽑아야할 개수가 정해지지 않은 조합임!!!!!!!!!
# 부분집합 구하는것과 같음 
# 매번 DFS 마다, 해당 원소가 들어가는 다음 DFS / 안들어가는 다음 DFS 나눠서 실행


def DFS(n,Ssum,Tsum):
    global max 
    if Tsum > M:
        return 
    if n == N:
        if Ssum > max : max = Ssum 
    else:
        DFS(n+1,Ssum+arr[n][0],Tsum+arr[n][1])
        DFS(n+1,Ssum,Tsum)


max = 0
N,M = map(int,input().split())
arr=[]
for i in range(N):  
    s,t = map(int,input().split())
    arr.append((s,t))
ch = [0]*N 
DFS(0,0,0)
print(max)

