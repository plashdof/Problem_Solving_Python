
# 내풀이
# 결과 : Fail
# BFS 아직 경험이 없어, DFS로 접근해보았으나 실패.
# 재귀가 너무 많아 TimeLimit 및 에러발생한다

def DFS(n,x):
    global min 
    if x==E:
        if min > n: min = n
        return  
    else:
        if x < E:
            DFS(n+1,x+5)
            DFS(n+1,x+1)
        else:
            DFS(n+1,x-1)
        
        

min = 21470000
S,E = map(int,input().split())
DFS(0,S)
print(min)


# 수정풀이
# BFS 를 활용. 
# BFS 는 Queue 와 While 문 활용한다

# 방문노드 체크 배열 & 횟수체크 배열 필요함


from collections import deque
MAX = 10000

ch = [0] * (MAX+1)
dis = [0] * (MAX+1)

S,E = map(int,input().split())

# 지나온 노드 체크
ch[S] = 1

# Start 부터의 횟수 체크
dis[S] = 0

dQ = deque()
dQ.append(S)
while dQ:
    now = dQ.popleft()
    if now==E:
        break
    for next in (now-1, now+1, now+5):
        # dis, ch 배열 벗어나지 않고,  지나온 노드가 아닐때
        if 1 <= next <= MAX and ch[next]== 0:
            # Queue 에 삽입, ch 체크, dis 표시.
            dQ.append(next)
            ch[next] = 1
            dis[next] = dis[now]+1
                
print(dis[E])