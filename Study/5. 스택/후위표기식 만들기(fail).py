
text = input()
stack = []
for i in text:
    if i.isdecimal():
        print(i,end="")
    else:
        if i == '(':
            stack.append(i)
        elif i == '+' or i == '-':
            while stack and stack[-1] != '(':
                print(stack.pop(),end="")
            stack.append(i)
        elif i == '*' or i == '/':
            # * 나 / 는 괄호로 감쌀 필요가 없기때문에, 마지막 조건을 뺴도 된다!!
            while stack and stack[-1] != '+' and stack[-1] != '-' and stack[-1] != '(':
                print(stack.pop(),end="")
            stack.append(i)
        elif i == ')':
            while stack and (stack[-1] != '('):
                print(stack.pop(),end="")
            stack.pop()

while stack:
    print(stack.pop(),end="")



