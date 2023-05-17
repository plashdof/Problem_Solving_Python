
# pop / insert / append 활용 잘하기

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
M = int(input())

for i in range(M):
    rownum, side, rotate = map(int,input().split())
    move = rotate % N 
    if side == 1:
        for i in range(move):
            x = arr[rownum-1].pop()
            arr[rownum-1].insert(0,x)
    else:
        for i in range(move):
            x = arr[rownum-1].pop(0)
            arr[rownum-1].append(x)

s = 0
e = N-1
answer = 0
for index, l in enumerate(arr):
    answer+=sum(l[s:e+1])
    if(index >= N//2):
        s-=1
        e+=1
    else:
        s+=1
        e-=1
print(answer)

    



    