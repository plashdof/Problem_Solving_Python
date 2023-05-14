import math 

def is_prime(x):
    if(x == 1):
        return False
    if(x == 2):
        return True 
    temp = math.sqrt(x)
    temp = math.ceil(temp)
    for i in range(2, temp+1):
        if x % i == 0:
            return False 
    return True 

N = int(input())
count = 0
for i in range(1, N+1):
    if(is_prime(i)):
        count+=1
print(count)


# 에라토스테네스 체 방식으로 풀기
# 1 ~ n 자연수중 소수 개수 구하기

# n=int(input())
# ch=[0]*(n+1)
# cnt=0
# for i in range(2, n+1):
#     if ch[i]==0:
#         cnt+=1
#         for j in range(i, n+1, i):    # i 가 소수면, i의 배수들을 0에서 1로 변경!
#             ch[j]=1
# print(cnt)


