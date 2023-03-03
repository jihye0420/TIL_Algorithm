# https://school.programmers.co.kr/learn/courses/30/lessons/86051
from typing import List


def solution(numbers: List[int]) -> int:
    answer: int = 0
    zero_to_nine: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    # * 방법1: 반복문 이용하기
    # for i in zero_to_nine:
    #     answer += i
    # for j in numbers:
    #     answer -= j
    # * 방법2: 리스트 차집합 이용하기
    complement: List[int] = list(set(zero_to_nine) - set(numbers))
    for i in complement:
        answer += i
    return answer


if __name__ == '__main__':
    print(solution([1, 2, 3, 4, 6, 7, 8, 0]))
    print(solution([5, 8, 4, 0, 6, 7, 9]))
