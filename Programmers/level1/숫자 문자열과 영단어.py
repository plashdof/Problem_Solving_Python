### 내풀이

# 접근법 : 한자리 숫자의 영단어는 3,4,5자리밖에 없다.
# 문자를 만나면 우선, 3,4,5자리를탐색후 맞는 숫자로 변환시키면 된다



def solution(s):
    dict = {"zero":0, "one":1, "two":2,
            "three":3, "four":4, "five":5,
            "six":6, "seven":7, "eight":8,
            "nine":9}
    arr = list(dict.keys())
    ans = []
    for i,x in enumerate(s):
        if x.isalpha():
            temp1 = s[i:i+3]
            temp2 = s[i:i+4]
            temp3 = s[i:i+5]
            if temp1 in arr:
                ans.append(dict[temp1])
            elif temp2 in arr:
                ans.append(dict[temp2])
            elif temp3 in arr:
                ans.append(dict[temp3])
        else:
            ans.append(int(x))
    count=0
    answer = 0
    for i in ans[::-1]:
        answer+= pow(10,count)*i
        count+=1

    return answer

print(solution("one4seveneight"))