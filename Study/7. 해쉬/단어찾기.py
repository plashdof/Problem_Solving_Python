N = int(input())
myDict = dict()
for i in range(N):
    voc = input()    
    myDict[voc]=1

for i in range(N-1):
    voc = input()
    myDict[voc]=0

keys = myDict.keys()
for i in keys:
    if myDict[i] == 1:
        print(i)

# keys로 반환된 key들로, key에 해당되는 value 찾는게 시간 오래걸릴 수도 있음!
# items로 for문 돌려서, value 가 1인 key 프린트하면 됨

# for key, value in myDict.items():
    
    

    

    

    



    





