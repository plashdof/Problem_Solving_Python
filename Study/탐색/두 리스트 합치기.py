
N = int(input())
arrN = list(map(int,input().split()))
M = int(input())
arrM = list(map(int,input().split()))

arrNew = arrN + arrM 
arrNew.sort()
for i in arrNew:
    print(i,end=" ")