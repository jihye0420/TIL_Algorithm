# https://school.programmers.co.kr/learn/courses/30/lessons/12909?language=python3
from collections import Counter


def solution(s):
    answer = True
    s = list(s)
    # print(s)
    tmp = Counter(s)
    temp_list = []
    # print(tmp)
    # keys = tmp.keys()
    # values = tmp.values()
    # print(keys)
    # print(values)
    # print(tmp['('])

    if tmp['('] != tmp[')']:
        answer = False
    if s[0] == ')':
        answer = False
    if s:
        for i in s:
            if i == '(':
                temp_list.append(i)
            elif i == ')':
                if temp_list:
                    temp_list.pop(-1)
                else:
                    answer = False
    return answer


if __name__ == '__main__':
    print(solution("()()"))  #
    print(solution(")()("))
