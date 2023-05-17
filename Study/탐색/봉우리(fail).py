N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
arr.insert(0,[0]*N)
arr.append([0]*N)
for i in arr:
    i.append(0)
    i.insert(0,0)

## all 활용 숙지
## 브루트 포스하게 해도 timelimit 안남

dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

cnt=0
for i in range(1, N+1):
    for j in range(1, N+1):
        if all(arr[i][j]>arr[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt+=1
print(cnt)

# arr[i+dx[k]][j+dy[k]] for k in range(4) 이부분은

# for k in range(4):
#     arr[i+dx[k]][j+dy[k]]   이와 같다




    



    