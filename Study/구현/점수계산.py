
N = int(input())
arr = list(map(int,input().split()))

score = 0
count = 0
for i in arr:
    if i == 1:
        score = score + 1 + count 
        count+=1
    elif i == 0:
        count = 0
print(score)