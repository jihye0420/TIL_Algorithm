# https://school.programmers.co.kr/learn/courses/30/lessons/12909
from collections import Counter


def solution(s: str) -> bool:
    answer: bool = True
    s: list = list(s)
    c: Counter = Counter(s)
    temp_list = []
    print(s)
    # * 괄호 개수 확인
    # * 맨 앞과 맨 뒤 확인
    # * stack에 넣고 팝하기
    if c['('] != c[')']:
        answer = False
    if s[0] != '(' or s[-1] != ')':
        answer = False
    for i in s:
        if i == '(':
            temp_list.append(i)
        elif i == ')':
            if not temp_list:
                answer = False
                break
            elif temp_list[-1] == ')':
                answer = False
                break
            else:
                temp_list.pop(-1)
    if temp_list:
        answer = False
    return answer


if __name__ == '__main__':
    print(solution("()()"))
    print(solution("(())()"))
    print(solution(")()("))
    print(solution("(()("))
