# todo: 다른 사람 풀이보기
# todo: 정확성 : 10.5
# https://school.programmers.co.kr/learn/courses/30/lessons/155652
# * 아스키: 알파벳을 비롯한 문자들을 통신하기 위해 일대일 대응시켜 숫자로 정해둔 코드
# ! 아스키 코드 <-> 문자
# ord(문자) : 아스키 코드로 변환
# chr(아스키 코드) : 문자로 변환
def solution(s, skip, index):
    answer = ''
    for i in s:
        temp = 0
        while temp < index:
            if i not in skip:
                if ord(i) == 122:
                    i = 'a'
                    temp += 1
                else:
                    i = ord(i) + 1
                    i = chr(i)
                    temp += 1
            else:
                if ord(i) == 122:
                    i = 'a'
                    continue
                else:
                    i = ord(i) + 1
                    i = chr(i)
                    continue
        answer += i

    return answer


if __name__ == '__main__':
    print(solution("aukks", "wbqd", 5))
