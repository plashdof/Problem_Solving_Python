
# python 은 C++ 처럼, 문자간의 연산이 바로 아스키코드로 반환되지 않음.
# 따라서, 각 문자 ord 로 아스키코드를 반환시킨후 연산해야함

text = input()
next = input()
arr = [0]*60

for i in text:
    arr[ord(i) - ord("A")]+=1

for i in next:
    if arr[ord(i) - ord("A")] == 0:
        print("NO")
        break 
    else:
        arr[ord(i) - ord("A")]-=1
else:
    print("YES")


    
# Dictionary 사용법!!

a=input()
b=input()
sH=dict()
for x in a:
    sH[x]=sH.get(x, 0)+1
for x in b:
    sH[x]=sH.get(x, 0)-1

for x in a:
    if sH.get(x) > 0:
        print("NO")
        break 
else:
    print("YES")


    





