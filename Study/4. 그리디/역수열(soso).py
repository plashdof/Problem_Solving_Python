N = int(input())
arr = list(map(int,input().split()))
answer = [0]*N 

for i, x in enumerate(arr):
    data = i+1
    count = x
    for index,j in enumerate(answer):
        if count == 0 and j == 0:
            answer[index] = data 
            break 
        if j == 0: count-=1

for i in answer:
    print(i,end=" ")


# for문 이렇게 돌리면 더 간편해짐!!   

# n=int(input())
# a=list(map(int, input().split()))
# seq=[0]*n
# for i in range(n):
#     for j in range(n):
#         if(a[i]==0 and seq[j]==0):
#             seq[j]=i+1
#             break
#         elif seq[j]==0:
#             a[i]-=1

# for x in seq:
#     print(x, end=' ')