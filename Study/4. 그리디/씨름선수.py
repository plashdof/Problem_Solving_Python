N = int(input())
arr = []
for _ in range(N):
    h,w = map(int,input().split())
    arr.append((h,w))

arr.sort(reverse=True)

count = 1
index = 1
maX = arr[0][1]

while index != len(arr):
    if maX < arr[index][1]:
        count+=1
        maX = arr[index][1]
    index+=1

print(count)

    
# 키순서대로 정렬후, 
# 바로 뒷순서가 앞순서보다 몸무게 많이나가면 maX업데이트 & count 증가




# 좀더 간단화 한 방법

# n=int(input())
# body=[]
# for i in range(n):
#     a, b=map(int, input().split())
#     body.append((a, b))
# body.sort(reverse=True)
# largest=0
# cnt=0
# for x, y in body:
#     if y>largest:
#         largest=y
#         cnt+=1
# print(cnt)







    



    