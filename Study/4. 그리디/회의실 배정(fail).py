n = int(input())
arr = []
for _ in range(n):
    s, e = map(int,input().split())
    arr.append((s,e))
arr.sort(key=lambda x : (x[1],x[0]))

end = arr[0][1]
count = 1
for i in arr:
    if i[0] >= end:
        count+=1
        end = i[1]
print(count)


# 회의 끝나는 시간 기준으로 정렬해야함
# 빨리끝나는 회의부터 앞으로 오게끔!!!

# 앞에놓인 회의 끝시간 vs 뒤에놓인 회의 시작시간 비교

# 뒤에놓인 회의 시작시간이 
# #크거나 같으면 회의 가능
# #작으면 회의 불가능. 버리기











    



    