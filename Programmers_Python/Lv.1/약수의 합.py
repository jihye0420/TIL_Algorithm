# https://school.programmers.co.kr/learn/courses/30/lessons/12928
def solution(n):
    answer = 0
    for i in range(1, n + 1):
        if n % i == 0:
            answer += i
        else:
            continue
    return answer


if __name__ == '__main__':
    print(solution(12))
    print(solution(5))
