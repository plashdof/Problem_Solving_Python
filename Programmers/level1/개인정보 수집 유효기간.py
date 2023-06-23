### 기존 내풀이
### 결과 : 17 / 19 번 test case 실패  나머지 성공

# today 는 "2022.05.19" 형태
# terms 는 ["A 6", "B 12", "C 3"] 형태
# privacies 는 ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"] 형태


# 우선 terms로 dictionary 생성

# privacies for문 돌려서, 마지막글자와, 앞글자 공백으로 나눈다음
# terms dictionary에서 숫자 꺼내서, 유효기간 만료날짜 계산
# 만료날짜와 today 비교 -> 파기해야되면 answer 배열에 담기




def solution(today, terms, privacies):
    dict={}
    answer = []
    for term in terms:
        key, value = term.split()
        dict[key] = value

    ty,tm,td = map(int,today.split('.'))

    for index,data in enumerate(privacies):
        date, value = data.split()
        y,m,d = map(int,date.split('.'))

        new_month = m + int(dict[value])
        new_year = y
        if new_month >=13:
            temp = new_month // 12
            temp2 = new_month % 12
            new_year += temp  
            new_month = temp2 
        new_date = d - 1  
        if d == 1:
            new_date = 28

        if ty > new_year:
            answer.append(index+1)
        elif ty == new_year and tm > new_month:
            answer.append(index+1)
        elif ty == new_year and tm == new_month and td > new_date:
            answer.append(index+1)
            
    return answer



today_input = "2022.05.19"
terms_input = ["A 6", "B 12", "C 3"]
privacies_input = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

print(solution(today_input, terms_input, privacies_input))


### 수정풀이

# 조건문들을 최소화하면서 정확도를 높이려면, 년,월을 일로 바꾸어서, 단순 int 값 비교를 해줘야 한다

def solution(today, terms, privacies):
    dict={}
    answer = []
    for term in terms:
        key, value = term.split()
        dict[key] = int(value)
    
    todayInt = changeToDay(today)

    for index,data in enumerate(privacies):
        date, value = data.split()
        limitInt = changeToDay(date)
        limitInt = limitInt + dict[value] * 28

        if limitInt <= todayInt:
            answer.append(index+1)
            
    return answer


def changeToDay(data):
    y,m,d = map(int,data.split('.'))
    result = (y * 28 * 12) + (m * 28) + d 
    return result 