# https://school.programmers.co.kr/learn/courses/30/lessons/12924
# todo: 완전 탐색 문제 & 문제 유형 파악하기
def solution(n: int) -> int:
    answer = 0

    for i in range(1, n + 1):  # 1 ~ n까지
        sum_val = 0
        for j in range(i, n + 1):  # 1 ~ n까지
            sum_val += j
            if sum_val == n:
                answer += 1
            elif sum_val > n:
                break
    return answer


if __name__ == '__main__':
    print(solution(15))
