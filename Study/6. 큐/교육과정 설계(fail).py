def study(text):
    cnt = 0 
    for i in text:
        if i == x[cnt]:
            cnt+=1
            if cnt == max:
                return "YES"
    return "NO"


x = input()
N = int(input())
max = len(x)
arr = []
for i in range(N):
    text = input()
    arr.append(text)

for i,data in enumerate(arr):
    print("#{0} {1}".format(i+1,study(data)))

# 고려 못한것 : 뒷순서의 과목이 앞순서보다 먼저나올때!! 
# ex)  CBA 인데,  AABBBCBA 이런거






# 필수과목을 deque에 삽입

# x in dq 를 이용해서, dq안에 있는 과목인지 탐색
# 있는 과목이면, dq pop 해서, 순서 일치하는지 탐색
from collections import deque
    
            

need =input()
N = int(input())
result = []
for i in range(N):
    data = input()
    dq = deque(need)
    for x in data:
        if x in dq:
            if x != dq.popleft():
                break 
    if dq:
        result.append("NO")
    else:
        result.append("YES")

for i, data in enumerate(result):
    print("#{0} {1}".format(i+1,data))
    

    

    

    



    





