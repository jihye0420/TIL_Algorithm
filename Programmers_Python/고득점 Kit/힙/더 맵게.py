# https://school.programmers.co.kr/learn/courses/30/lessons/42626
"""
# * 나의 풀이 => 테스트 케이스 실패 (정확성, 효율성 실패)
# 정확성: 48.4
# 효율성: 0.0
# 합계: 48.4 / 100.0
"""
import heapq


def solution(scoville, k):
    answer = 0

    # h = []
    # result = []
    # for i in scoville:
    #     heapq.heappush(h, i)

    # 힙을 만드는 과정이 아래 코드로 대체됨
    heapq.heapify(scoville)

    hot = 0
    while scoville[0] < k:
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        hot = a + b * 2
        answer += 1
        if hot >= k:
            break
        else:
            heapq.heappush(scoville, hot)
        # ! 아래 h의 개수, k보다 작은지의 여부를 확인 =>
        if len(scoville) == 1 and scoville[0] < k:
            return -1
    return answer


"""
# * 다른 사람 풀이 => 정확한 풀이
"""

# ! 구현
# import heapq
#
#
# def solution(scoville, k):
#     answer = 0
#     # 기존 리스트 -> 최소 힙으로!
#     heapq.heapify(scoville)
#
#     #
#     while scoville[0] < k:
#         mix = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
#         heapq.heappush(scoville, mix)
#         answer += 1
#         if len(scoville) == 1 and scoville[0] < k:
#             return -1
#     return answer


if __name__ == '__main__':
    print(solution(scoville=[1, 2, 3, 9, 10, 12], k=7))
