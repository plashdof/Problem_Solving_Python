text = input()
stack = []

for i in text:
    if i.isdecimal():
        stack.append(i)
    else:
        x1 = int(stack.pop())
        x2 = int(stack.pop())
        if i == '+':
            stack.append(x1 + x2)
        elif i == '-':
            stack.append(x2 - x1)
        elif i == '*':
            stack.append(x1 * x2)
        elif i == '/':
            stack.append(x2 / x1)

print(stack[0])




