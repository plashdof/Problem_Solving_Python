
N = int(input())
arr = []
for i in range(N):
    temp = list(map(int, input().split()))
    arr.append(temp)

max = 0

# 행 합
for i in range(N):
    sum = 0
    for j in arr[i]:
        sum+=j 
    if sum > max: max = sum 

# 열 합
for i in range(N):
    sum = 0
    for j in range(N):
        sum+= arr[j][i]
    if sum > max: max = sum 

# 좌->우 대각 합
sum = 0
for i in range(N):
    sum+= arr[i][i]
if sum > max: max = sum 

# 우->좌 대각 합
sum = 0
for i in range(N):
    for j in range(N-1,0):
        sum+= arr[i][j]
if sum > max: max = sum 
print(max)

    

## 정해
## 한 반복문에서, 열합과 행합을 같이 진행
## 한 반복문에서, 좌->우 대각합과  우->좌 대각합 같이 진행

# N = int(input())
# arr = [list(map(int,input().split())) for _ in range(N)]
# max = 0

# for i in range(N):
#     colsum=rowsum=0
#     for j in range(N):
#         rowsum+=arr[i][j]
#         colsum+=arr[j][i]
#     if colsum > rowsum: max = colsum
#     else: max = rowsum 

# leftsum=rightsum=0
# for i in range(N):
#     leftsum+=arr[i][i]
#     rightsum+=arr[i][N+i-1]
# if leftsum > max : max = leftsum 
# if rightsum> max : max = rightsum 
# print(max)
