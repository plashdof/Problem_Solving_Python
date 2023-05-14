
Max = 0
N = int(input())
for i in range(N):
    arr = list(map(int,input().split()))
    score = 0
    if(arr[0] == arr[1] & arr[1]== arr[2]):
        score = 10000 + arr[0]*1000
    elif(arr[0] == arr[1]):
        score = 1000 + arr[0] *100
    elif(arr[1] == arr[2]):
        score = 1000 + arr[1]*100 
    elif(arr[0] == arr[2]):
        score = 1000 + arr[0]*100
    else:
        max = 0
        for i in arr:
            if i > max:
                max = i 
        score = max*100 
        
    if score > Max: 
        Max = score

print(Max) 


# sort로 배열을 정렬하고 순서를 안뒤 시작하면, 코드길이를 줄일수 있음

# max=0
# res=0
# n=int(input())
# for i in range(n):
#     tmp=input().split() 
#     tmp.sort() 
#     a, b, c=map(int, tmp)
#     if a==b and b==c:
#         money=10000+(a*1000);
#     elif a==b or a==c:
#         money=1000+(a*100)
#     elif b==c:
#         money=1000+(b*100)
#     else:
#         money=c*100
#     if money > res:
#         res=money



