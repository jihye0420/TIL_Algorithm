# https://school.programmers.co.kr/learn/courses/30/lessons/131701
import typing
from typing import List, Set


def solution(elements: List[int]):
    answer: int = 0
    temp_set: Set[int] = set()
    for i in range(1, len(elements) + 1):
        for j in range(i + 1):
            elements[j]
    return answer


if __name__ == '__main__':
    print(solution([7, 9, 1, 1, 4]))
