def count(arr, mid):
    counting = 0
    for i in arr:
        counting += i // mid
    return counting

K,N = map(int,input().split())
arr = []
for i in range(K):
    temp = int(input())
    arr.append(temp)
arr.sort(reverse=True)
max = arr[0]

lt = 1
rt = max
answer = 0
while lt <= rt:
    # 이분탐색처럼 mid = N 되면 while 탈출이 아니라, 더 큰 값 찾아서 다시 돌려야함
    mid = (lt + rt) //2
    temp = count(arr,mid)
    if temp < N:
        rt = mid-1
    else:
        answer = mid
        lt = mid+1
        

print(answer)






# 내 풀이. 브루트포스 하게 찾는 알고리즘 적용됨

# K,N = map(int,input().split())
# arr = []
# for i in range(K):
#     temp = int(input())
#     arr.append(temp)
# arr.sort()
# min = arr[0]


# 여기까진 문제 없지만,  min을 전부 조사하는게 아님, 이분탐색으로 조사한다!

# while min!=0:
#     answer = 0
#     for i in arr:
#         answer += i // min 
    
#     if answer == N:
#         print(min)
#         break 

#     min-=1













    



    