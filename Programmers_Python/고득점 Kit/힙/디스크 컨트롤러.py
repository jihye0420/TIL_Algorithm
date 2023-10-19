# https://school.programmers.co.kr/learn/courses/30/lessons/42627
"""
# 힙 활용하는 방법 정리
"""
import heapq


def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1
    heap = []

    while i < len(jobs):
        # 현재 시점에서 처리할 수 있는 작업을 heap에 저장 => 작업의 소요 시간을 기준으로 최소힙을 구성
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])  # [작업의 소요 시간, 작업이 요청되는 시점]
        # print(heap)
        if len(heap) > 0:  # 처리할 작업이 있는 경우
            current = heapq.heappop(heap)
            start = now  # 현재 시간
            now += current[0]  # 현재 시간에서 작업의 소요 시간 더하기
            answer += now - current[1]  # 작업 요청시간부터 종료시간까지의 시간 계산
            i += 1
        else:  # 처리할 작업이 없는 경우 다음 시간을 넘어감
            now += 1

    return answer // len(jobs)


if __name__ == '__main__':
    print(solution([[0, 3], [1, 9], [2, 6]]))
