# https://school.programmers.co.kr/learn/courses/30/lessons/67257
def solution(expression: str):
    answer = 0
    temp = []
    # 수식 기준 자르기
    # 나올 수 있는 조합 먼저 뽑기 -> 계산 한 수 중 가장 큰 값을 answer로 !
    for i in ['-', '+', '*']:
        if i in expression:

    print(expression)
    return answer


if __name__ == '__main__':
    print(solution("100-200*300-500+20"))
    # [100, -, 200, *, 300, -, 500, +, 20]
