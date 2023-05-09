# todo: 다른사람 풀이보기
# https://school.programmers.co.kr/learn/courses/30/lessons/42578
# from itertools import combinations
#
#
# def solution(clothes):
#     answer = 0
#     for i in combinations(clothes[0], 1):
#         print(i)
#     return answer
#
#
# if __name__ == '__main__':
#     print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))


from collections import Counter
from functools import reduce

def solution(clothes):
    # 1. 의상 종류별 Counter를 만든다.
    counter = Counter([type for clothe, type in clothes])

    # 2. 모든 종류의 count + 1을 누적하여 곱해준다
    answer = reduce(lambda acc, cur: acc*(cur+1), counter.values(), 1) - 1
    return answer

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))