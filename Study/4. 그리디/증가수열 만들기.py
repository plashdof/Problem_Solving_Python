N = int(input())
arr = list(map(int,input().split()))
answer = ""
lt = 0
rt = N-1
temp = 0
while lt <= rt:
    Min = min(arr[lt], arr[rt])
    Max = max(arr[lt], arr[rt])
    if temp > Max:
        break 

    if Min == arr[lt] :
        if Min > temp:
            temp = arr[lt]
            answer+= 'L'
            lt+=1
        else:
            temp = arr[rt]
            answer+= 'R'
            rt-=1
    else:
        if Min > temp:
            temp = arr[rt]
            answer+= 'R'
            rt-=1
        else:
            temp = arr[lt]
            answer+= 'L'
            lt+=1
    

print(len(answer))
print(answer)


 
# 왼, 오른값 모두 이전값 보다 작으면, break

# 왼, 오른 중 작은값 선택

# 작은값이 이전값보다 작으면, 다른값 선택
# 작은값이 이전값보다 크면, 해당값 선택



# 튜플로 tmp에 넣은뒤, 숫자값 기준으로 sorting.
# 만약 tmp에 아무것도 안들어갔다면, last가 가장 큰수이므로, break
# res 에 tmp를 옮겨담기

# n=int(input())
# a=list(map(int, input().split()))
# lt=0
# rt=n-1
# last=0
# res=""
# tmp=[]
# while lt<=rt:
#     if a[lt]>last:
#         tmp.append((a[lt], 'L'))
#     if a[rt]>last:
#         tmp.append((a[rt], 'R'))
#     tmp.sort()
#     if len(tmp)==0:
#         break;
#     else:
#         res=res+tmp[0][1]
#         last=tmp[0][0]
#         if tmp[0][1]=='L':
#             lt=lt+1
#         else:
#             rt=rt-1
#     tmp.clear()

# print(len(res))
# print(res)