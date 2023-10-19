# https://school.programmers.co.kr/learn/courses/30/lessons/43236
"""
* 나의 풀이 => 테스트 케이스는 맞음, but! 알고리즘이 없음.
정확성: 5.1
합계: 5.1 / 100.0
"""
from itertools import permutations, combinations, product, combinations_with_replacement


def solution(distance, rocks, n):  # 거리, 돌, 제거할 돌 개수
    # 조합(중복 x)
    rocks.sort()
    eliminate_rock = list(combinations(rocks, n))
    rocks.append(distance)
    rocks.sort()
    tt = []
    for i in eliminate_rock:
        temp = rocks.copy()
        temp.remove(i[0])
        temp.remove(i[1])
        temp.sort()
        t = []
        for j in range(0, len(temp)):
            if j == 0:
                t.append(temp[j] - 0)
            else:
                t.append(temp[j] - temp[j - 1])
        tt.append(min(t))
    return max(tt)

"""
# 다른 풀이

"""


if __name__ == '__main__':
    print(solution(25, [2, 14, 11, 21, 17], 2))
