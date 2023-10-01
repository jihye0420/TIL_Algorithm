# https://school.programmers.co.kr/learn/courses/30/lessons/12914
from itertools import permutations, product


def solution(n):
    answer = 0
    # 1 또는 2로 구성 가능!
    sets = [1, 2]

    data = []

    for i in range(1, n + 1):
        data.append(list(product(sets, repeat=i)))
    # print(data)
    # print(len(data))

    for j in range(0, n):
        # print(data[j])
        for k in data[j]:
            # print(k)
            if sum(k) == n:
                answer += 1
    return answer


if __name__ == '__main__':
    print(solution(4))
    print(solution(3))
