# https://school.programmers.co.kr/learn/courses/30/lessons/12914
from itertools import permutations, product


def solution(n):
    answer = 0
    # 1 또는 2로 구성 가능!

    sets = [1, 2]
    # result_3 = list(product(data, repeat=2))
    data = [0] * 10000

    for i in range(1, n + 1):
        data[i] = list(product(sets, repeat=i))

    # print(data)
    for i in data:
        print(i)
        # if sum(i) == n:
        #     answer += 1

    return answer


if __name__ == '__main__':
    print(solution(4))
    # print(solution(3))
