# https://school.programmers.co.kr/learn/courses/30/lessons/42586
import math


def solution(progresses: list, speeds: list):
    answer = []

    # 1. 남은 작업량 계산하여 배포일 알기
    days = []
    for (p, s) in zip(progresses, speeds):
        temp = 100 - p
        days.append(math.ceil(temp / s))

    index = 0
    # 2. 남은 일보다 큰 값이 나타났을 때 인덱스 값을 계산하여 넣기
    for i in range(len(days)):
        if days[index] < days[i]:
            answer.append(i - index)
            index = i
    answer.append(len(days) - index)
    return answer


if __name__ == '__main__':
    print(solution(progresses=[93, 30, 55], speeds=[1, 30, 5]))
    print(solution(progresses=[95, 90, 99, 99, 80, 99], speeds=[1, 1, 1, 1, 1, 1]))
