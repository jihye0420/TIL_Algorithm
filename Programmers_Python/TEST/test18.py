def solution(numbers, k):
    def count_swaps(arr):
        n = len(arr)
        swaps = 0
        sorted_arr = sorted(arr)
        index_map = {value: index for index, value in enumerate(arr)}

        for i in range(n):
            if arr[i] != sorted_arr[i]:
                swaps += 1
                curr = arr[i]
                arr[i], arr[index_map[sorted_arr[i]]] = sorted_arr[i], curr
                index_map[curr] = index_map[sorted_arr[i]]
                index_map[sorted_arr[i]] = i

        return swaps

    def check_adjacent_difference(arr, k):
        for i in range(1, len(arr)):
            if abs(arr[i] - arr[i - 1]) > k:
                return False
        return True

    def generate_permutations(arr, start, result):
        if start == len(arr):
            result.append(arr.copy())
        else:
            for i in range(start, len(arr)):
                arr[start], arr[i] = arr[i], arr[start]
                generate_permutations(arr, start + 1, result)
                arr[start], arr[i] = arr[i], arr[start]

    permutations = []
    generate_permutations(numbers, 0, permutations)
    min_swaps = float('inf')

    for permutation in permutations:
        if check_adjacent_difference(permutation, k):
            swaps = count_swaps(permutation)
            min_swaps = min(min_swaps, swaps)

    return min_swaps


if __name__ == '__main__':
    print(solution([10, 40, 30, 20], 20))
    print(solution([3, 7, 2, 8, 6, 4, 5, 1], 3))
