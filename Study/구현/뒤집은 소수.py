import math 

## 1은 무조건 소수가 아니다
## 2는 무조건 소수이다

def reverse(x):
    text = str(x)
    text = text[::-1]
    num = int(text)
    return num 

def isPrime(x):
    if(x == 1):
        return False
    if(x == 2):
        return True
    temp = math.sqrt(x)
    temp = math.ceil(temp)
    for i in range(2,temp+1):
        if(x % i == 0):
            return False  
    return True


N = int(input())
nums = list(map(int,input().split()))

for i in nums:
    num = reverse(i)
    if(isPrime(num)):
        print(num,end=" ")




