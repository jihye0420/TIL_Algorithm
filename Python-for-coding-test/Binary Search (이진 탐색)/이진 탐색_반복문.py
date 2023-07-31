n, find = map(int, input().split())
print(n)
print(find)
data = list(map(int, input().split()))


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        elif array[mid] > target:
            end = mid - 1
    return None


result = binary_search(data, find, 0, n - 1)
if not result:
    print("찾는 값이 없습니다.")
else:
    print(result + 1)
