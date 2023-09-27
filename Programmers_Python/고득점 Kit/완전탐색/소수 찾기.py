# https://school.programmers.co.kr/learn/courses/30/lessons/42839
# * 배운점 : 소수 찾기 알고리즘
from itertools import permutations


# 소수 판별 함수(2이상의 자연수에 대하여)
def is_prime_number(x):
    if x == 0 or x == 1:
        return False
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, x):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False  # 소수가 아님
    return True  # 소수임


def solution(numbers):
    answer = []

    n = list(numbers)

    list_temp = []
    for j in range(len(n) + 1):
        for p in permutations(n, j):
            if not p:
                continue
            list_temp.append(''.join(p))
    # print(list_temp)
    for i in range(len(list_temp)):
        list_temp[i] = int(list_temp[i])
        if is_prime_number(list_temp[i]):
            answer.append(list_temp[i])
    answer = set(answer)
    return len(answer)


if __name__ == '__main__':
    print(solution("17"))
    print(solution("011"))
