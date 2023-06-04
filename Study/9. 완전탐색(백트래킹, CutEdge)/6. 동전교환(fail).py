# 내풀이
# 결과 : TimeLimits
def DFS(n,sum,cnt):
    global Min 
    if Min < cnt:
        return 
    if sum > M:
        return 
    if sum == M:
        if Min > cnt: Min = cnt 
    else:
        for i in arr:
            DFS(n+1, sum+i,cnt+1)


Min = 2147000000
N = int(input())
arr = list(map(int,input().split()))
M = int(input())
DFS(0,0,0)
print(Min)





# 수정풀이

# 1. n 이 개수이므로, cnt 필요없음. n이 동전의 사용 개수
# 2. Min 초기값 2147000000 으로
# 3. 어차피 가장 작은 사용동전수 구하는거기 때문에,  동전배열 내림차순으로 설정

# Cut-Edge Skill
# Min 값이 n 보다 작거나 같으면, 재귀종료 (내림차순으로 설정한 이유)
# sum이 M 보다 크면, 재귀종료

def DFS(n,sum):
    global Min 
    if Min <= n:
        return 
    if sum > M:
        return 
    if sum == M:
        if Min > n: Min = n 
    else:
        for i in arr:
            DFS(n+1, sum+i)


Min = 2147000000
N = int(input())
arr = list(map(int,input().split()))
arr.sort(reverse=True)
M = int(input())
DFS(0,0)
print(Min)
