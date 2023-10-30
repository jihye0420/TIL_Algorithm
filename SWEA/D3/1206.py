for tc in range(1, 11):
    n = int(input())
    data = list(map(int, input().split()))
    result = 0

    for i in range(2, n - 2):
        left = max(data[i - 1], data[i - 2])
        right = max(data[i + 1], data[i + 2])
        if data[i] - left > 0 and data[i] - right > 0:
            max_value = max(left, right)
            result += data[i] - max_value
    print(f"#{tc}", result)
