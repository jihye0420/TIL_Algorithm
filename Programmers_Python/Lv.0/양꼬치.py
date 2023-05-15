# https://school.programmers.co.kr/learn/courses/30/lessons/120830
def solution(n: int, k: int) -> int:
    answer = 0
    answer = n * 12000 + k * 2000

    if (n // 10) != 0:
        answer -= (n // 10) * 2000
    return answer


if __name__ == '__main__':
    print(solution(10, 3))
    print(solution(64, 6))
