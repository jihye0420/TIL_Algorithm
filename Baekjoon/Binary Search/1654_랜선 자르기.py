# https://www.acmicpc.net/problem/1654
# * 실버 2
"""
* 아이디어
- 이분 탐색 : 런타임 에러 발생...
* 알게된 점
"""
import sys

input = sys.stdin.readline

k, n = map(int, input().split())
data = [int(input()) for i in range(k)]
# for i in range(k):
#     data.append(int(input()))
data.sort()

result = 0  # mid값을 저장
left, right = 0, max(data)

while left <= right:
    total = 0  # 총 개수
    mid = (left + right) // 2
    for i in data:
        if i // mid > 0:
            total += i // mid
    if total >= n:  # 필요한 랜선의 개수가 많다면 - 자르는 단위의 길이가 짧다는 것  => 오른쪽 탐색
        result = mid
        left = mid + 1
    else:  # 필요한 랜선의 개수가 적다면 - 자르는 단위의 길이가 길다는 것 (최대 랜선의 길이 저장) => 왼쪽 탐색
        right = mid - 1
print(result)
