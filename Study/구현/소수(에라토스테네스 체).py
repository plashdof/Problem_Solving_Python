import math 

def is_prime(x):
    if(x == 1):
        return False
    if(x == 2):
        return True 
    temp = math.sqrt(x)
    temp = math.ceil(temp)
    for i in range(2, temp+1):
        if x % i == 0:
            return False 
    return True 

N = int(input())
count = 0
for i in range(1, N+1):
    if(is_prime(i)):
        count+=1
print(count)






