# https://school.programmers.co.kr/learn/courses/30/lessons/42627
import heapq


def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1
    heap = []

    while i < len(jobs):
        for j in jobs:
            # 현재 시간에 요청이 들어온 작업만 힙에 저장 => 최소 시간의 작업이 우선 순위!
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])
        # 힙에서 꺼내서 작업
        if len(heap) > 0:
            current = heapq.heappop(heap)  # 작업 소요되는 시간, 요청이 들어온 시간
            start = now
            now += current[0]
            answer += now - current[1]
            i += 1
        else:
            now += 1

    return answer // len(jobs)


if __name__ == '__main__':
    print(solution([[0, 3], [1, 9], [2, 6]]))
