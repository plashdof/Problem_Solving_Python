# 나보다 작은숫자가 나보다 앞에있으면 안됨
# 앞에있는 숫자가 나보다 작으면, 지우기!!

num, N = map(int,input().split())
arr = list(map(int, str(num)))
stack=[]
for i in arr:
    while stack and N>0 and stack[-1] < i:
        stack.pop()
        N-=1
    stack.append(i)

# .N이 0이 아니라면 뒤에서 남은 N번째 까지 짤라준다
if N!=0:
    stack = stack[:-N]

for i in stack:
    print(i,end="")




