from itertools import permutations

N, K = map(int, input().split())
arr = list(map(int,input().split()))
sumArr = []
for i in permutations(arr,3):
    sum = 0
    for j in i:
        sum += j 
    sumArr.append(sum)
sumArr = list(set(sumArr))
sumArr.sort(reverse=True)
print(sumArr[K-1])

