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
        temp = rocks.copy()  # 파이썬 리스트 복사 => 얕은 복사
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
# 다른 풀이 => 이분 탐색 알고리즘 추가
"""


def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)

    low = 1
    high = distance

    answer = 0

    while low <= high:
        mid = (low + high) // 2  # 최솟값

        cur_rock = 0  # 왼쪽 바위
        count = 0  # 제거된 수
        for i in range(len(rocks)):
            pre_rock = rocks[i]  # 오른쪽 바위

            if pre_rock - cur_rock < mid:  # mid보다 작을 경우 제거한다.
                count += 1

            else:
                cur_rock = pre_rock

            if n < count:
                break

        if count <= n:  # mid가 클수록 제거해야 하는 돌이 늘어난다.
            answer = mid
            low = mid + 1

        else:
            high = mid - 1

    return answer


if __name__ == '__main__':
    print(solution(25, [2, 14, 11, 21, 17], 2))
