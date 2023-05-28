import heapq as hq 

arr = []
while True:
    num = int(input())
    if num == -1:
        break 
    elif num == 0:
        print(hq.heappop(arr))
    else:
        hq.heappush(arr,num)

    

    

    



    





