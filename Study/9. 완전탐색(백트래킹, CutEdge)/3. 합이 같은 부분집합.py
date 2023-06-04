
# 내풀이

import sys

def DFS(n):
    if n == N:
        sum1 = 0
        sum2 = 0
        for i,data in enumerate(ch):
            if data == 1:
                sum1+=arr[i]
            else:
                sum2+=arr[i] 
        if sum1 == sum2:
            print("YES")
            sys.exit(0)
    else:
        ch[n] = 1
        DFS(n+1)
        ch[n] = 0
        DFS(n+1)



N = int(input())
arr = list(map(int,input().split())) 
ch = [0]*(N)
DFS(0)
print("NO")



## ch 배열 사용하지 않는방법

# DFS의 인자를 두개설정해서, 
# 한개는 sum 에 값을 더하고 한개는 더하지 않으면,  두개의 부분집합 형성하면서 만들어진다
# 또한, 배열의 초기 total 값을 이용해, total - sum 과 sum 을 비교하여 답을 도출한다

# 또한, sum 이 total의 절반보다 클 경우, 재귀를 계속하지않고 종료시켜 시간복잡도를 줄임!!

import sys 

def DFS(n,sum):
    if sum > total//2:
        return 
    elif n==N:
        if sum == (total - sum):
            print("YES")
            sys.exit(0)
    else:
        DFS(n+1,sum+arr[n])
        DFS(n+1,sum)
        
N = int(input())
arr = list(map(int,input().split()))
total = sum(arr)
DFS(0,0)
print("NO")




