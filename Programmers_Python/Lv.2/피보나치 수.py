# todo: 다시 풀어보기
# https://school.programmers.co.kr/learn/courses/30/lessons/12945
def f(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return f(n - 1) + f(n - 2)


def solution(n):
    tmp_answer = 0
    tmp_answer += f(n)
    answer = tmp_answer % 1234567
    return answer


if __name__ == '__main__':
    print(solution(3))
    print(solution(5))
