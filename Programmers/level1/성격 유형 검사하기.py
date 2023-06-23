### 내풀이
### 결과 : 한번에 통과!

# 딕셔너리 활용
# R:점수, T:점수, ... 이런식

# RT  /  CF  /  JM  /  AN


# survey 와 choices를 index로 같은 for문에 돌리기
# AN 이면은, 초이스 1,2,3 이    A + 4 - 초이스값
# 	   초이스 5,6,7 이   N + 초이스값 - 4 
# 이렇게 저장만 해주면 됨


def solution(survey, choices):
    answer = ''
    dict = {'R':0, 'T':0,'C':0,'F':0,
            'J':0,'M':0,'A':0,'N':0}
    for i in range(len(survey)):
        if choices[i] < 4:
            dict[survey[i][0]] += 4 - choices[i]
        elif choices[i] > 4:
            dict[survey[i][1]] += choices[i] - 4

    if dict['R'] >= dict['T']: answer+='R'
    else: answer+='T'

    if dict['C'] >= dict['F']: answer+='C'
    else: answer+='F'

    if dict['J'] >= dict['M']: answer+='J'
    else: answer+='M'

    if dict['A'] >= dict['N']: answer+='A'
    else: answer+='N'

    
    return answer