# https://school.programmers.co.kr/learn/courses/30/lessons/43165
# 참고: https://namhandong.tistory.com/143
from collections import deque

"""
# BFS 풀이
"""
# def solution(numbers, target):
#     count = 0
#     queue = deque()
#     queue.append((0, 0))
#     while queue:
#         current_sum, index = queue.popleft()
#
#         if index == len(numbers):
#             if current_sum == target:
#                 count += 1
#         else:
#             current_number = numbers[index]
#             queue.append((current_sum + current_number, index + 1))
#             queue.append((current_sum - current_number, index + 1))
#     return count


"""
# DFS 풀이
"""
answer = 0


def dfs(idx, numbers, target, value):
    global answer
    N = len(numbers)
    if idx == N:
        if target == value:
            answer += 1
            return
    else:
        dfs(idx + 1, numbers, target, value + numbers[idx])
        dfs(idx + 1, numbers, target, value - numbers[idx])


def solution(numbers, target):
    global answer
    dfs(0, numbers, target, 0)
    return answer


if __name__ == '__main__':
    print(solution([1, 1, 1, 1, 1], 3))
