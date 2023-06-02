
# 두번째 버전. 이래도 TimeLimit 발생한다!

def DFS(n,sum):
    global max 
    if sum > C:
        return
    if n == N:
        if max < sum: max = sum 
    else:
        DFS(n+1,sum+arr[n])
        DFS(n+1,sum)

max = 0

C, N = map(int,input().split())
arr=[]
for i in range(N):
    temp = int(input())
    arr.append(temp)
DFS(0,0)
print(max)


# Cut Edge 기술!

# totalsum 은, 판단을 이미 한(이미 지나온) 원소들의 합
# total - totalsum 은, 앞으로 남아있는 판단해야될 원소들의 합

# 만약, 현재까지합 + 남아있는 모든 원소의 합이 max 보다 작다면
# 더이상 진행해야될 필요가 없음!!!

def DFS(n,sum, totalsum):
    global max 
    if sum + (total - totalsum) < max:
        return 
    if sum > C:
        return
    if n == N:
        if max < sum: max = sum 
    else:
        DFS(n+1,sum+arr[n], totalsum +arr[n])
        DFS(n+1,sum, totalsum + arr[n])

max = 0

C, N = map(int,input().split())
arr=[]
for i in range(N):
    temp = int(input())
    arr.append(temp)
total = sum(arr)
DFS(0,0,0)
print(max)



