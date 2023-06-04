
# 내풀이
# 결과 : Success

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


# 수정 풀이
# 1. 중복순열 구하는 부분, for문 대신 ch 중복체크 배열 활용
# 2. pascal  삼각형 결과값 나오는 부분, DFS 내부에서 처리!!
    # 규칙발견
    # 원소 4개면 -> 1 3 3 1 각원소 곱하기해서 더한값이 결과
    # 원소 5개면 -> 1 4 6 4 1 번 곱하기해서 더한값
    # 이항계수임!!! 5C1 5C2 5C3 5C4 5C5 값

    # N 받은뒤, 이항계수저장해놓는 배열 미리 생성

import sys

def DFS(n,sum):
    if n==N and sum == F:
        for i in res:
            print(i,end=" ")
        sys.exit(0)
    else:
        for i in range(1,N+1):
            if ch[i] == 0:
                ch[i] = 1
                res[n] = i 
                DFS(n+1,sum + (res[n] * ehang[n]))
                ch[i] = 0
N,F = map(int,input().split())
res = [0]*N
ehang = [1]*N
for i in range(1,N):
    # NCi 순열 구하는 식
    ehang[i] = ehang[i-1]*(N-i)//i  
ch = [0]*(N+1)
DFS(0,0)



# 다른 풀이
# permutations 메소드이용

import itertools as it

N, F=map(int, input().split())
ehang=[1]*N
cnt=0
for i in range(1, N):
    ehang[i]=ehang[i-1]*(N-i)/i

arr=list(range(1, N+1))
for temp in it.permutations(arr):
    sum=0
    for index, data in enumerate(temp):
        sum+=(data*ehang[index])
    if sum==F:
        for x in temp:
            print(x, end=' ')
        break