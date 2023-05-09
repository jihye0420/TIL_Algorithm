# https://school.programmers.co.kr/learn/courses/30/lessons/120910
def solution(n, t):
    answer = 0
    answer = n * 2 ** t
    return answer


if __name__ == '__main__':
    print(solution(2, 10))