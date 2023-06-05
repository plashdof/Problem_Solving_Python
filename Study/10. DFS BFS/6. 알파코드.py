
# 내풀이
# 결과 : Success
# 조건을 제대로 이해 못해서, 초반실수가 매우 많았다
# 0이면 입력종료를 뜻한다는것이, DFS 돌면서 0이 나오면 return 해주면 된다
# 대신 10 같은건 허용해야 되므로, temp[0] == '0'  이렇게 감별하자

def DFS(n):
    global cnt 
    if len(res)>0:
        temp = res.pop()
        if int(temp) > 26 or temp[0]=='0': 
            res.append(temp)
            return 
        res.append(temp)
    if n==size:
        cnt+=1
        for i in res:
            a = int(i)
            print(chars[a],end="")
        print()
        return 
    else:
        res.append(arr[n])
        DFS(n+1)
        res.pop()
        if n <= size-2:
            res.append(arr[n]+arr[n+1])
            DFS(n+2)
            res.pop()
        




cnt = 0
code = input()
size= len(code)
arr=[]
res=[]
chars="0ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in code: 
    arr.append(i)
DFS(0)
print(cnt)