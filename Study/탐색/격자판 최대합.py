
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

    