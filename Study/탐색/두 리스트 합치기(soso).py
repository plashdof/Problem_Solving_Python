
N = int(input())
arrN = list(map(int,input().split()))
M = int(input())
arrM = list(map(int,input().split()))

arrNew = arrN + arrM 
arrNew.sort()
for i in arrNew:
    print(i,end=" ")



# sort를 사용하지 않는 법
# sort는 nlogn 인데, n번만에 가능하다

# import sys
# sys.stdin=open("input.txt", "r")
# n=int(input())
# a=list(map(int, input().split()))
# m=int(input())
# b=list(map(int, input().split()))
# p1=p2=0
# c=[]
# while p1<n and p2<m:
#     if a[p1]<b[p2]:
#         c.append(a[p1])
#         p1+=1
#     else:
#         c.append(b[p2])
#         p2+=1
# if p1<n:
#     c=c+a[p1:]
# if p2<m:
#     c=c+b[p2:]
# for x in c:
#     print(x, end=' ')