# https://school.programmers.co.kr/learn/courses/30/lessons/12916
# def solution(s: str):
#     answer: bool = True
#     y_count: int = 0
#     p_count: int = 0
#     s.lower()
#     # print(s.lower())
#     for i in s.lower():
#         if i == 'y':
#             y_count += 1
#         elif i == 'p':
#             p_count += 1
#     # print(y_count, p_count)
#     if y_count == p_count:
#         answer = True
#     else:
#         answer = False
#     return answer


"""
# count() 함수를 이용한 다른 풀이 방식
"""


def solution(s):
    s = s.lower()
    return s.count('p') == s.count('y')


if __name__ == '__main__':
    print(solution("pPoooyY"))
    print(solution("Pyy"))
    print(solution("ooooooo"))
    print(solution("PPyy"))
