
arr = []
for i in range(1,21):
    arr.append(i)

for i in range(10):
    a, b = map(int, input().split())
    newArr = arr[a-1:b]
    newArr = newArr[::-1]
    index = 0
    for j in range(a-1,b):
        arr[j] = newArr[index]
        index+=1
for i in arr:
    print(i, end=" ")


# 짧은 풀이
# 역순 list를 새로 만드는게 아닌, for문으로 직접 교환시켜줌
# 교환이 끝난뒤 배열 맨앞 원소 pop 시켜줌


# import sys
# sys.stdin=open("input.txt", "r")
# a=list(range(21))
# for _ in range(10):
#     s, e=map(int, input().split())
#     for i in range((e-s+1)//2):
#         a[s+i], a[e-i]=a[e-i], a[s+i]
# a.pop(0)
# for x in a:
#     print(x, end=' ')