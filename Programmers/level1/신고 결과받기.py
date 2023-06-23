### 내풀이
### 통과

# 동일 유저 여러번 신고 -> 1회신고로 카운트

# A를 누가 신고했는지 set로 관리
# 각 유저가 몇번 신고당했는지 Int배열로 카운트값 저장

# k번이상 신고받은 유저 -> 신고한 유저들에게 메일발송

def solution(id_list, report, k):
    

    n = len(id_list)
    answer = [0] * n
    singoCount = [0]*n
    singoNuga = [set() for _ in range(n)]

    for data in report:
        a,b = data.split()
        index = id_list.index(b)
        if a in singoNuga[index]:
            pass 
        else:
            singoCount[index]+=1

        singoNuga[index].add(a)
    
    for i,data in enumerate(singoCount):
        if data >= k:
            for j in singoNuga[i]:
                index = id_list.index(j)
                answer[index]+=1
    

    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

print(solution(id_list,report,k))


# 처음에 배열안에 set 넣을떄,  [set()]*n 이렇게했었다.  이러면 모든 set이 같은주솟값을 같게 되는듯!!
# 그래서 [set() for _ in range(n)] 이렇게 해줘야됨!