
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