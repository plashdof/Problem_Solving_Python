
# 내풀이
# 결과 : Fail 
# 그래프 표현은 할줄알지만, DFS로 경로수 계산하는법 모르겠음

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


# 수정 풀이 (경로까지 print 하는 version)

# 1. 어떻게보면, 경로도 조합을 구하는것이므로, 중복제거 배열 ch 도입.
    # 한번 방문노드 방문 안하기 위함

# 2. 경로를 저장할 stack 인 path 도입
    # DFS 시작전 path 에 정점 append
    # DFS 끝나면 path 에 가장최근 정점 pop 
    # DFS 특성상 뒤로 한칸씩 back 하면서, 다시 탐색하기 때문


def DFS(v):
    global cnt, path
    if v==N:
        cnt+=1
        for x in path:
            print(x, end=' ')
        print()
    else:
        for i in range(1, N+1):
            if G[v][i]==1 and ch[i]==0:
                ch[i]=1
                path.append(i)
                DFS(i)
                path.pop()
                ch[i]=0
           
N, M=map(int, input().split())
G=[[0]*(N+1) for _ in range(N+1)]

# 중복제거 배열. 한번 방문노드 체크
ch=[0]*(N+1)
ch[1]=1
for i in range(M):
    a, b=map(int, input().split())
    G[a][b]=1

cnt=0

path=list()
path.append(1)
DFS(1)
print(cnt)


