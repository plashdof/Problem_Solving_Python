
def counting(x):
    count = 0
    for i in range(1,x+1):
        if x%i == 0:
            count+=1
    print(count)


text = input()
answer = ""
for i in text:
    if i.isdigit():
        answer += i 
answer = int(answer)
print(answer)
counting(answer)