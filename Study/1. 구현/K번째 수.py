

T = int(input())

for i in range(T):
    arr = []
    N,s,e,k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = arr[s-1:e]
    arr.sort()
    print("#{0} {1}".format(i+1, arr[k-1]))


# 슬라이싱 할때 몇번째 인지 잘 생각하기!