from typing import List

# class Solution:
#     answerSet = set()
#     sum = 0
#
#     def solution(self, k: int, numbers: List[int]) -> int:
#         self.permutation(numbers, 0, 0, k, len(numbers))
#
#         answer = min(self.answerSet) if self.answerSet else -1
#         # print(self.sum)
#         return answer
#
#     def permutation(self, numbers: List[int], depth: int, cnt: int, k: int, N: int) -> None:
#         if depth == N:
#             self.sum += 1
#             flag = True
#             for i in range(1, len(numbers)):
#                 if abs(numbers[i - 1] - numbers[i]) > k:
#                     flag = False
#                     break
#
#             if flag:
#                 self.answerSet.add(cnt)
#
#             # print(numbers)
#
#         for i in range(depth, N):
#             self.swap(numbers, depth, i)
#
#             if depth != i:
#                 self.permutation(numbers, depth + 1, cnt + 1, k, N)
#             else:
#                 self.permutation(numbers, depth + 1, cnt, k, N)
#
#             self.swap(numbers, depth, i)
#
#     @staticmethod
#     def swap(numbers: List[int], depth: int, i: int) -> None:
#         numbers[depth], numbers[i] = numbers[i], numbers[depth]


from typing import List, Set


def solution(numbers: List[int], k: int) -> int:
    answer_set: Set[int] = set()
    sum_count = 0

    def permutation(numbers: List[int], depth: int, cnt: int, k: int, N: int) -> None:
        nonlocal sum_count, answer_set

        if depth == N:
            sum_count += 1
            flag = all(abs(numbers[i - 1] - numbers[i]) <= k for i in range(1, len(numbers)))

            if flag:
                answer_set.add(cnt)

        for i in range(depth, N):
            numbers[depth], numbers[i] = numbers[i], numbers[depth]

            if depth != i:
                permutation(numbers, depth + 1, cnt + 1, k, N)
            else:
                permutation(numbers, depth + 1, cnt, k, N)

            numbers[depth], numbers[i] = numbers[i], numbers[depth]

    permutation(numbers, 0, 0, k, len(numbers))

    answer = min(answer_set) if answer_set else -1
    return answer


if __name__ == '__main__':
    print(solution([10, 40, 30, 20], 20))
    print(solution([3, 7, 2, 8, 6, 4, 5, 1], 3))
