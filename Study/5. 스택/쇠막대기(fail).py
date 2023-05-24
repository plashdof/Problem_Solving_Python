
# (( 가 되면, 첫번째 ( 는 쇠막대기이다
#  ) 가 등장하면, 바로앞이 ( 면 레이저이다

# )) 가 되면, 두번째 ) 는 쇠막대기 끝이다

# () 나타날때 OR )) 나타날때마다, 카운팅을 해주면 됨!!

text = input()
stack = ['x']
cnt = 0
res = 0
for i in text:
    if i == '(' and stack[-1] == '(':
       cnt+=1 
    elif i == ')' and stack[-1] == '(':
       res+=cnt 
    elif i == ')' and stack[-1] == ')':
       res+=1
       cnt-=1
    stack.append(i)
print(res)



# s=input()
# stack=[]
# cnt=0
# for i in range(len(s)):
#     if s[i]=='(':
#         stack.append(s[i])
#     else:
#         stack.pop()
#         if s[i-1]=='(':
#             cnt+=len(stack)
#         else:
#             cnt+=1
# print(cnt)