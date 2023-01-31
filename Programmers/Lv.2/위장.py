# todo: 다른사람 풀이보기
# https://school.programmers.co.kr/learn/courses/30/lessons/42578
from itertools import combinations


def solution(clothes):
    answer = 0
    for i in combinations(clothes[0], 1):
        print(i)
    return answer


if __name__ == '__main__':
    print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
