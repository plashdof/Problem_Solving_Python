
# temp = arr[j:j+5][i] 앞 행은 리스트가 아니라서 슬라이싱이 안됨!!!
# for문으로 처리!

arr = [list(map(int,input().split())) for _ in range(7)]

count = 0
for i in range(7):
    for j in range(3):
        temp = arr[i][j:j+5]
        if temp == temp[::-1]:
            count+=1
        temp = []
        for k in range(5):
            temp.append(arr[j+k][i])
        if temp == temp[::-1]:
            count+=1
        
print(count)


# <회문의 길이가 가변적일 때 코드>
# board=[list(map(int, input().split())) for _ in range(7)]
# cnt=0
# len=5
# for i in range(3):
#     for j in range(7):
#         tmp=board[j][i:i+len]
#         if tmp==tmp[::-1]:
#             cnt+=1
#         #tmp=board[i:i+5][j] 앞 행은 리스트가 아니라서 슬라이스가 안된다.
#         for k in range(len//2):
#             if board[i+k][j]!=board[len-k+i-1][j]:
#                 break;
#         else:
#             cnt+=1
        
# print(cnt)




    



    