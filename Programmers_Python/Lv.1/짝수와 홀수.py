# https://school.programmers.co.kr/learn/courses/30/lessons/12937
def solution(num):
    answer = ''
    if num % 2 == 1:
        answer = 'Odd'
    else:
        answer = 'Even'
    return answer


if __name__ == '__main__':
    print(solution(num=3))
    print(solution(num=4))
