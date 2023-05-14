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

# list 로 자료 담고 set 으로 중복제거 하는법 보다,
# set으로 자료담고, list로 바꾼뒤 sort 하는게 더 효율적일듯!!


# permutations 활용 하지 않는 방법
# res=set()
# for i in range(n):
#     for j in range(i+1, n):
#         for m in range(j+1, n):
#             res.add(a[i]+a[j]+a[m])

