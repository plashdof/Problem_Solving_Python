
def checkSudoku(arr):
    
    for i in range(9):
        checkrow = [0]*10
        checkcol = [0]*10
        for j in range(9):
            if checkrow[arr[i][j]] == 0 : checkrow[arr[i][j]] = 1
            else: 
                return False 
            if checkcol[arr[j][i]] == 0 : checkcol[arr[j][i]] = 1
            else: 
                return False
            
    
    xs= ys = 0
    xe = ye = 2
    while True:
        checkgroup = [0]*10
        for i in range(ys, ye+1):
            for j in range(xs, xe+1):
                if checkgroup[arr[i][j]] == 0 : checkgroup[arr[i][j]] = 1
                else: 
                    return False 
        if xe == 8:
            xs = 0
            xe = 2
            ys+=3
            ye+=3
        else:
            xs+=3
            xe+=3
        
        if ye == 8 and xe == 8:
            return True 
        
    

arr = [list(map(int,input().split())) for _ in range(9)]
if checkSudoku(arr):
    print("YES")
else:
    print("NO")


# 4중 For문 이용

# def check(a):
#     for i in range(9):
#         ch1=[0]*10
#         ch2=[0]*10
#         for j in range(9):
#             ch1[a[i][j]]=1
#             ch2[a[j][i]]=1
#         if sum(ch1)!=9 or sum(ch2)!=9:
#             return False
#     for i in range(3):
#         for j in range(3):
#             ch3=[0]*10
#             for k in range(3):
#                 for s in range(3):
#                     ch3[a[i*3+k][j*3+s]]=1
#             if sum(ch3)!=9:
#                 return False
#     return True









    



    