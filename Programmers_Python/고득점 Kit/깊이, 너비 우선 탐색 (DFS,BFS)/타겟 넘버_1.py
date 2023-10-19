from collections import deque

answer = 0


def dfs(numbers, num, sum, target):
    global answer
    if sum == target and num == len(numbers):
        answer += 1
    if num >= len(numbers):
        return
    dfs(numbers, num + 1, sum + numbers[num], target)
    dfs(numbers, num + 1, sum - numbers[num], target)


def bfs(numbers, target):
    answer = 0
    queue = deque()
    queue.append([0, 0])

    while queue:
        idx, v = queue.popleft()

        if idx < len(numbers):
            queue.append([idx + 1, v + numbers[idx]])
            queue.append([idx + 1, v - numbers[idx]])

        if idx == len(numbers) and v == target:
            answer += 1
    return answer


def solution(numbers, target):
    global answer
    dfs(numbers, 0, 0, target)
    # answer = bfs(numbers, target)
    return answer


if __name__ == '__main__':
    # print(solution([1, 1, 1, 1, 1], 3))
    print(solution([4, 1, 2, 1], 4))
