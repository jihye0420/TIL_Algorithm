# https://school.programmers.co.kr/learn/courses/30/lessons/12914
from itertools import permutations, product

"""
나의 풀이
"""
# def solution(n):
#     answer = 0
#     # 1 또는 2로 구성 가능!
#     sets = [1, 2]
#
#     data = []
#
#     for i in range(1, n + 1):
#         data.append(list(product(sets, repeat=i)))
#     print("data: ", data)
#     print(len(data))
#
#     for j in range(0, n):
#         # print(data[j])
#         for k in data[j]:
#             # print(k)
#             if sum(k) == n:
#                 answer += 1
#     return answer


"""
다른 풀이 : DP 테이블 활용해보기
"""


def solution(n):
    # n까지 뛰는 방법을 저장하기 위한 배열
    dp = [0] * (n + 1)

    dp[0] = 1
    dp[1] = 2

    for i in range(2, n):
        dp[i] = dp[i - 2] + dp[i - 1]

    return dp[n - 1] % 1234567


if __name__ == '__main__':
    print(solution(4))
    print(solution(3))
