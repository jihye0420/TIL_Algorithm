# https://school.programmers.co.kr/learn/courses/30/lessons/42626
import heapq


def solution(scoville, k):
    answer = 0
    h = []
    result = []
    for i in scoville:
        heapq.heappush(h, i)
    # for j in range(len(h)):
    #     result.append(heapq.heappop(h))
    hot = 0
    while h:
        a = heapq.heappop(h)
        b = heapq.heappop(h)
        hot = a + b * 2
        answer += 1
        if hot >= k:
            break
        else:
            heapq.heappush(h, hot)

    return answer


if __name__ == '__main__':
    print(solution(scoville=[1, 2, 3, 9, 10, 12], k=7))
