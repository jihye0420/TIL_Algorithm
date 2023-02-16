# 구현 중
from itertools import permutations


def solution(n):
    answer = -1
    numbers = [6, 2, 5, 5, 4, 5, 6, 4, 7, 6]
    operator = [2, 1, 1, 2]
    permu = list(permutations(numbers, 3))
    temp_list = []
    tmp = {
        0: [],
        1: [],
        2: [],
        3: [],
    }
    for a, b, c in permu:
        temp_list.append(a + b + c)

    for i, o in enumerate(operator):
        n -= o
        for idx, t in enumerate(temp_list):
            if t == n:
                tmp[i].append(idx)

    for k, v in enumerate()

    for i in range(tmp):
        for tt in tmp[i]:
            aa, bb, cc = temp_list[tt]

    return answer


if __name__ == '__main__':
    print(solution(21))
    # print(solution(0))
