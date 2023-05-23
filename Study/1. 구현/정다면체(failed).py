
N, M = map(int, input().split())

# 눈의 합을 인덱스로 사용

arr = [0]*(N+M+3)

for i in range(1,N+1):
    for j in range(1,M+1):
        arr[i+j]+= 1

max = 0
for i in range(2,N+M+3):
    if arr[i] > max:
        max = arr[i]

for i in range(2,N+M+3):
    if arr[i] == max:
        print(i, end=" ")


