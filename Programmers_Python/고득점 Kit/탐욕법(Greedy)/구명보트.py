# https://school.programmers.co.kr/learn/courses/30/lessons/42885
from collections import deque
from typing import List


def solution(people: List, limit: int):
    answer = 0
    people = deque(sorted(people, reverse=True))
    # print(people.popleft())
    while len(people) > 1:
        if people[0] + people[-1] <= limit:  # 최대와 최소를 빼기
            answer += 1
            people.pop()  # 최소 빼기
            people.popleft()  # 최대 빼기
        else:
            answer += 1
            people.popleft()
    if people:  # people에 1명 남아있는 경우 처리
        answer += 1
    return answer


if __name__ == '__main__':
    print(solution([70, 50, 80, 50], 100))
    print(solution([70, 80, 50], 100))
