N = int(input())
arr = []
for i in range(N):
    temp = list(map(int,input().split()))
    arr.append(temp)
s = N // 2
e = N // 2
middle = N // 2 
answer = 0

for index, l in enumerate(arr):
    answer += sum(l[s:e+1])
    if index >= middle:
        s+=1
        e-=1
    else:
        s-=1
        e+=1
print(answer)


# 코드 줄이기

# N = int(input())
# arr = [list(map(int,input().split())) for _ in range(N)]
# s = e 
# answer = 0

# for index, l in enumerate(arr):
#     answer += sum(l[s:e+1])
#     if index >= N//2:
#         s+=1
#         e-=1
#     else:
#         s-=1
#         e+=1
# print(answer)


    