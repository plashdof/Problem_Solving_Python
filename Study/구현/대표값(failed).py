
N = int(input())
arr = list(map(int,input().split()))
avg = round(sum(arr) / N) 
print(avg,end=" ")
min = 100
minScore = 0
minIndex = 0
for i, score in enumerate(arr):
    if abs(score-avg) == min:
        if(score > minScore):
            minScore = score
            min = abs(score-avg)
            minIndex = i
    elif abs(score-avg) < min:
        minScore = score 
        min = abs(score-avg)
        minIndex = i

print(minIndex+1)

