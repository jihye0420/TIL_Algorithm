import itertools
from itertools import permutations


def calculate_swap_count(arr):
    sorted_arr = sorted(arr)
    swap_count = 0
    index_map = {value: index for index, value in enumerate(arr)}

    for i in range(len(arr)):
        if arr[i] != sorted_arr[i]:
            swap_count += 1
            curr = arr[i]
            arr[i], arr[index_map[sorted_arr[i]]] = sorted_arr[i], curr
            index_map[curr] = index_map[sorted_arr[i]]
            index_map[sorted_arr[i]] = i

    return swap_count


def find_minimum_swaps(numbers, k):
    permutations_temp = list(permutations(numbers))
    min_swap_count = []

    for permutation in permutations_temp:
        valid = True
        for i in range(1, len(permutation)):
            if abs(permutation[i] - permutation[i - 1]) > k:
                valid = False
                break

        if valid:
            swap_count = calculate_swap_count(list(permutation))
            print(swap_count)
            min_swap_count = min(min_swap_count, swap_count)

    # print(swap_count)

    return min_swap_count


if __name__ == '__main__':
    # print(solution([10, 40, 30, 20], 20))
    # print(solution([3, 7, 2, 8, 6, 4, 5, 1], 3))

    numbers = [10, 40, 30, 20]
    k = 20
    min_swaps = find_minimum_swaps(numbers, k)
    print("Minimum swaps:", min_swaps)
