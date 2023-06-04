
def DFS(v):
    if v==n+1:
        for i in range(1, n+1):
            if ch[i]==1:
                print(i, end=' ')
        print()
    else:
        ch[v]=1
        DFS(v+1)
        ch[v]=0
        DFS(v+1)

if __name__=="__main__":
    n=int(input())
    ch=[0]*(n+1)
    DFS(1)

# 한가지 원소가 들어갈지 / 들어갈지 말지  2가지 경우의수 있다
# 원소 만날때마다, 원소 사용하는지, 안하는지 두가지 branch 로 뻣어나감


# 원소가 들어갈지 말지 나타내는 ch 배열 선언
# ch[원소] = 1 -> 사용하는 것
# ch[원소] = 0 -> 사용하지 않는것





