
# 내풀이
# 결과 : Success

def DFS(n,start):
    if n==K:
        global cnt 
        temp = sum(res)
        if temp % M == 0:
            cnt+=1
    else:
        for i in range(start,N):
            res[n] = arr[i]
            DFS(n+1, i+1)

cnt=0
N,K = map(int,input().split())
arr = list(map(int,input().split()))
M = int(input())
res=[0]*K
DFS(0,0)
print(cnt)



# 수정풀이
# DFS 결과값의 sum 을 구해야하는 문제는, 과정 저장하는 res 배열 만들지 말고
# DFS 인자에 sum값을 넘겨주는것이 더 효율적!

def DFS(n,start,sum):
    if n==K:
        global cnt 
        if sum % M == 0:
            cnt+=1
    else:
        for i in range(start,N):
            DFS(n+1, i+1, sum+arr[i])

cnt=0
N,K = map(int,input().split())
arr = list(map(int,input().split()))
M = int(input())
DFS(0,0,0)
print(cnt)




# 다른풀이
# itertools 의 combinations 메소드 이용

import itertools as it
N, K=map(int, input().split())
arr=list(map(int, input().split()))
M=int(input())
cnt=0
for x in it.combinations(arr, K):
    if sum(x) % M==0:
        cnt+=1
print(cnt)