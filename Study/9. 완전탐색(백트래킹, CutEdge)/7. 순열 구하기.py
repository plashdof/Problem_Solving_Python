
# 내풀이
# 결과: Success
def DFS(n):
    if n == M:
        global cnt 
        cnt+=1
        for i in res:
            print(i,end=" ")
        print()
    else:
        for i in range(1,N+1):
            for j in range(n+1):
                if i == res[j]:
                    break
            else:
                res[n] = i 
                DFS(n+1)

cnt=0
N,M = map(int,input().split())
res = [0]*M 
DFS(0)
print(cnt)



# 수정풀이
# 중복체크리스트 생성! (for문으로 res안의 값과 일일이 대조하는거 비효율적임!!!)
# 중복체크하는 for문 제거
def DFS(n):
    if n == M:
        global cnt 
        cnt+=1
        for i in res:
            print(i,end=" ")
        print()
    else:
        for i in range(1,N+1):
            if ch[i] == 0:
                # 해당숫자 체크
                ch[i] = 1 
                res[n] = i 
                DFS(n+1)

                # DFS 끝나면 체크풀기! (다음 DFS에서 사용)
                ch[i] = 0

cnt=0
N,M = map(int,input().split())
res = [0]*M 
ch = [0] * (N+1)
DFS(0)
print(cnt)
