# https://school.programmers.co.kr/learn/courses/30/lessons/12903
def solution(s):
    answer = ''
    if len(s) % 2 == 1:
        answer = s[len(s) // 2]
    else:
        answer = s[len(s) // 2 - 1] + s[len(s) // 2]
    return answer


if __name__ == '__main__':
    print(solution('abcde'))
    print(solution('qwer'))
