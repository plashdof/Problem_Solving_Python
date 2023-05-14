

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









