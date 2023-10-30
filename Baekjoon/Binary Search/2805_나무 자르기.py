# https://www.acmicpc.net/problem/2805
# * 실버 2
"""
* 아이디어
* 알게된 점
- mid 값을 result에 최댓값, 최솟값을 보고 조건별로 지정하는 방법
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

left, right = 0, max(data)

result = 0
while left <= right:
    total = 0
    mid = (left + right) // 2
    for i in data:
        if i > mid:
            total += i - mid
    if total < m:  # 자른 나무가 더 적어서 부족한 경우 => 더 많이 잘라야 하므로 왼쪽 탐색
        right = mid - 1
    else:  # 자른 나무가 더 많거나 같은 경우 => 최댓값을 구해야하므로 result값을 일단 저장, 더 적게 잘라야 하므로 오른쪽 탐색
        result = mid
        left = mid + 1
print(result)
