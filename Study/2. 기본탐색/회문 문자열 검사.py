N = int(input())

for i in range(N):
    text = input()
    text = text.lower()
    temp = text[::-1]
    if text == temp:
        print("#{0} YES".format(i+1))
    else:
        print("#{0} NO".format(i+1))
