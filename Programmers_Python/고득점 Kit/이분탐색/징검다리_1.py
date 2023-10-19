def solution(distance, rocks, n):  # 거리, 돌, 제거할 돌 개수
    answer = 0

    # 커트라인 최솟값 = 1
    left = 1
    # 커트라인 최댓값 = distance
    right = distance

    # 바위 위치를 정렬하고, 도착지점 append
    rocks.sort()
    rocks.append(distance)

    while left <= right:
        mid = (left + right) // 2  # 최솟값
        prev_rock = 0  # 이전 바위 위치
        delete = 0  # 제거된 바위 수
        for rock in rocks:
            dist = rock - prev_rock
            # 거리가 커트라인 보다 작다면, 바위를 제거
            if dist < mid:
                delete += 1
                # 제거한 바위가 너무 많다면 break
                if delete > n:
                    break
            # 바위를 제거하지 않았다면, prev_rock을 갱신
            else:
                prev_rock = rock
        if delete > n:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1
    return answer


if __name__ == '__main__':
    print(solution(25, [2, 14, 11, 21, 17], 2))
