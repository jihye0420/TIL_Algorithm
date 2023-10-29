# https://www.acmicpc.net/problem/1920
# * 실버 4
"""
* 아이디어
- 단순 반복으로 구현 시 -> 시간 초과 발생
- 이분 탐색
* 알게된 점
- list를 정렬하지 않고 set으로 만들어 탐색하는 방법!
"""
import sys

input = sys.stdin.readline

n = int(input())
data = set(map(int, input().split()))

m = int(input())
check = list(map(int, input().split()))
for i in check:
    if i in data:
        print(1)
    else:
        print(0)

"""
이분탐색으로 문제풀기
"""
# 입력
n = int(input())
a = list(map(int, input().split()))
m = int(input())
arr = list(map(int, input().split()))
a.sort()  # a 정렬

for num in arr:
    left, right = 0, n - 1
    isExist = False  # 찾음 여부

    while left <= right:
        mid = (left + right) // 2
        if num == a[mid]:
            isExist = True
            print(1)
            break
        elif num < a[mid]:
            right = mid - 1
        elif num > a[mid]:
            left = mid + 1
    if isExist == False:
        print(0)
