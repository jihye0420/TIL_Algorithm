def solution(ball, order):
    answer = []
    queue = [-1, -1]
    for n in order:
        if ball[0] == n:
            answer.append(ball.pop(0))

            while ball:
                for index in range(-1, -len(queue) + 1, -1):
                    if queue[index] == ball[0]:
                        answer.append(ball.pop(0))
                        queue.pop(index)
                        break
                else:
                    break

        elif ball[-1] == n:
            answer.append(ball.pop(-1))

            while ball:
                for index in range(-1, -len(queue) + 1, -1):
                    if queue[index] == ball[-1]:
                        answer.append(ball.pop(-1))
                        queue.pop(index)
                        break
                else:
                    break

        else:
            queue.insert(2, n)

    return answer


# def solution(ball, order):
#     answer = []
#     stack = []
#     queue = deque(ball) # 큐
#     print(queue)
#     while True:
#         if not stack:
#             break
#         for i in order:
#             if i == queue.pop():
#                 queue.pop()
#                 answer.append(i)
#             elif i == queue.popleft():
#                 queue.popleft()
#                 answer.append(i)
#             if stack:
#                 if stack.pop(-1) == queue.pop():
#                     queue.pop()
#                     answer.append(stack.pop(-1))
#                 elif stack.pop(-1) == queue.popleft():
#                     queue.popleft()
#                     answer.append(stack.pop(-1))
#             else:
#                 stack.append(i)
#     return answer


if __name__ == '__main__':
    print(solution([1, 2, 3, 4, 5, 6], [6, 2, 5, 1, 4, 3]))
