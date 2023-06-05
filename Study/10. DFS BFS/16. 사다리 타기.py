
# 내 풀이
# 결과 : Success
# 문제 잘 파악하자. 사다리타기라서, 아래로 내려가다가 왼 or 오른쪽 1일떄 그쪽으로 빠져야함
# 오른쪽으로 가는중엔, 오른쪽으로만 가야하므로, 그 상태를 'R' 'L' state 으로 관리했음
# 방향 컨트롤이 되므로, check 이중배열은 사용하지 않았음

import sys

def DFS(y,x):
    global state 
    if x==-1 or y==-1 or x==10 or y==10:
        return
    if arr[y][x] == 0:
        return  
    if arr[y][x] == 2:
        print(start)
        sys.exit(0)
    else:
        if state == 'R':
            if x<9 and arr[y][x+1] == 1:
                DFS(y,x+1)
            else:
                state = ''
                DFS(y+1,x)
        elif state == 'L':
            if x>0 and arr[y][x-1] == 1:
                DFS(y,x-1)
            else:
                state = ''
                DFS(y+1,x)
        else:
            if x<9 and arr[y][x+1] == 1:
                state = 'R'
                DFS(y,x+1)
            elif x>0 and arr[y][x-1] == 1:
                state = 'L'
                DFS(y,x-1)
            else: 
                DFS(y+1,x)


arr = []
state = ''
for i in range(10):
    tt = list(map(int,input().split()))
    arr.append(tt)
start = 0

for i in range(10):
    if arr[0][i] == 1:
        start = i 
        DFS(0,i)
