
Max = 0
N = int(input())
for i in range(N):
    arr = list(map(int,input().split()))
    score = 0
    if(arr[0] == arr[1] & arr[1]== arr[2]):
        score = 10000 + arr[0]*1000
    elif(arr[0] == arr[1]):
        score = 1000 + arr[0] *100
    elif(arr[1] == arr[2]):
        score = 1000 + arr[1]*100 
    elif(arr[0] == arr[2]):
        score = 1000 + arr[0]*100
    else:
        max = 0
        for i in arr:
            if i > max:
                max = i 
        score = max*100 
        
    if score > Max: 
        Max = score

print(Max) 






