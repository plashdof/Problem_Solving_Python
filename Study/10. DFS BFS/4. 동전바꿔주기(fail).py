# 내풀이
# 결과 : fail
# 조합으로 풀게되면, 10,10,10 인상황에서,  똑같은 경우이지만 카운팅이 3번된다는것 감안하지 못함

def DFS(n,sum):
    global cnt 
    if sum > T:
        return 
    if n == size:
        if sum == T: cnt+=1
        return
    else:
        DFS(n+1,sum+arr[n])
        DFS(n+1,sum)


cnt = 0
T = int(input())
k = int(input())
arr = []
p = list()
for i in range(k): 
    p, n = map(int,input().split())
    for j in range(n):
        arr.append(p)
size = len(arr)
DFS(0,0)
print(cnt)

# 수정 내풀이
# 결과 : Success
# 동전금액, 동전개수를 따로 배열에 저장한뒤,  동전 금액별로, count 변화시켜 다중상태트리로 구현

def DFS(n,sum):
    global cnt 
    if sum > T:
        return
    if n==k:
        if sum==T:
            cnt+=1
        return 
    else:
        for i in range(count[n]+1):
            DFS(n+1,sum+(price[n]*i)) 


cnt = 0
T = int(input())
k = int(input())
price = []
count = []
for i in range(k): 
    p, n = map(int,input().split())
    price.append(p)
    count.append(n)

DFS(0,0)
print(cnt)

