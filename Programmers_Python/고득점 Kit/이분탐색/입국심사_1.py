def solution(n, times):
    answer = 0
    left = min(times)
    right = max(times) * n
    while left <= right:
        mid = (left + right) // 2
        checked = 0  # 심사 가능한 사람 수
        for time in times:
            checked += mid // time
            if checked >= n:
                break
        if checked >= n:
            answer = mid
            right = mid - 1
        elif checked < n:
            left = mid + 1

    return answer


if __name__ == '__main__':
    print(solution(6, [7, 10]))
