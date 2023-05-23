

def digit_sum(x):
    text = str(x)
    sum = 0
    for i in range(len(text)):
        sum += int(text[i])
    return sum 


N = int(input())
arr = list(map(int,input().split()))
max = 0
maxNum = 0

for i in arr:
    if(digit_sum(i)>max):
        max = digit_sum(i)
        maxNum = i

print(maxNum) 


# 형변환 없이 아래로직으로 자릿수합 가능
# while x>0:
#     sum+=x%10
#     x=x//10







