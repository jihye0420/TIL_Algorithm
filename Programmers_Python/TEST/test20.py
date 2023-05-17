# def solution(numbers, k):
#     swaps = 0
#     num_positions = {num: pos for pos, num in enumerate(numbers)}
#     sorted_nums = sorted(numbers)
#
#     for i in range(len(numbers)):
#         current_num = numbers[i]
#         sorted_num = sorted_nums[i]
#
#         if current_num != sorted_num:
#             while abs(current_num - sorted_num) >= k:
#                 try:
#                     swap_num = next(
#                         num for num in range(sorted_num - 1, current_num, -1)
#                         if num in num_positions and abs(num - current_num) < k
#                     )
#                     swap_pos = num_positions[swap_num]
#
#                     numbers[i], numbers[swap_pos] = numbers[swap_pos], numbers[i]
#                     num_positions[current_num], num_positions[swap_num] = swap_pos, i
#                     swaps += 1
#
#                     current_num = numbers[i]
#                     sorted_num = sorted_nums[i]
#                 except Exception as e:
#                     swaps = -1
#                     return swaps
#
#     return swaps
#
#
# if __name__ == '__main__':
#     print(solution([10, 40, 30, 20], 20))
#     print(solution([3, 7, 2, 8, 6, 4, 5, 1], 3))

# def solution(numbers, k):
#     swaps = 0  # Initialize the swap counter
#     n = len(numbers)
#
#     for i in range(n - 1):
#         if abs(numbers[i+1] - numbers[i]) > k:
#             j = i + 1
#             while j < n and abs(numbers[j] - numbers[i]) > k:
#                 j += 1
#             if j == n:
#                 return -1  # It's not possible to satisfy the condition
#             swaps += j - (i + 1)
#             numbers[i], numbers[j] = numbers[j], numbers[i]
#
#     return swaps




# def min_swaps(numbers, k):
#     swaps = 0  # Initialize the swap counter
#     n = len(numbers)
#
#     for i in range(n - 1):
#         if numbers[i+1] - numbers[i] > k:
#             j = i + 1
#             while j < n and numbers[j] - numbers[i] > k:
#                 j += 1
#             if j == n:
#                 return -1  # It's not possible to satisfy the condition
#             swaps += j - (i + 1)
#             numbers[i], numbers[j] = numbers[j], numbers[i]
#
#     return swaps

def min_swaps(numbers, k):
    swaps = 0  # Initialize the swap counter
    n = len(numbers)

    for i in range(n - 1):
        min_val = numbers[i] + k
        min_idx = -1

        for j in range(i + 1, n):
            if numbers[j] <= min_val:
                min_val = numbers[j]
                min_idx = j

        if min_idx == -1:
            return -1  # It's not possible to satisfy the condition

        swaps += min_idx - i
        numbers[i+1:min_idx+1] = numbers[i:min_idx]

    return swaps


if __name__ == '__main__':
    print(min_swaps([10, 40, 30, 20], 20))
    print(min_swaps([3, 7, 2, 8, 6, 4, 5, 1], 3))