# https://www.acmicpc.net/problem/10773
# * 실버 4
"""
* 아이디어
- 나만의 풀이 => 시간초과
    1. 리스트 => 시간초과
    2. 딕셔너리로 풀어보기 => 통과
    3. 이분탐색 => 시간초과
* 알게된 점
- dict 관련 함수
    - dict.keys() : Key 리스트 만들기
    - dict.values() : value 리스트 만들기
    - dict.items() : Key, Value 쌍 얻기
    - dict.clear() : Key: Value 쌍 모두 지우기
    - dict.get(key) : Key로 Value 얻기, key가 없을 시 None 리턴
    - for key in dict : 해당 Key가 딕셔너리 안에 있는지 조사하기
"""
n = int(input())
# data = list(map(int, input().split()))
temp = list(map(int, input().split()))
data = {}
m = int(input())
check = list(map(int, input().split()))

for i in temp:
    if i not in data.keys():
        data[i] = 1
    else:
        data[i] += 1

for i in check:
    print(data[i] if i in data.keys() else 0, end=' ')
"""
* 나만의 풀이
이분 탐색 => 결국 완탐임
"""
# n = int(input())
# data = list(map(int, input().split()))
# data.sort()
#
# m = int(input())
# check = list(map(int, input().split()))
#
# for i in check:
#     count = 0
#     check_num = 0
#     left = 0
#     right = n - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#         if i == data[mid]:
#             count += 1
#             for j in data[:mid]:
#                 if i == j:
#                     count += 1
#             for j in data[mid + 1:]:
#                 if i == j:
#                     count += 1
#             break
#         elif i < data[mid]:
#             right = mid - 1
#         elif i > data[mid]:
#             left = mid + 1
#     print(count, end=' ')
"""
* 다른 풀이
이분 탐색
"""
import sys

input = sys.stdin.readline

N = int(input())
cards = sorted([map(int, input().split())])
M = int(input())
candidate = [map(int, input().split())]

count = {}
for card in cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1


def binarySearch(arr, target, start, end):
    if start > end:
        return 0

    mid = (start + end) // 2
    if arr[mid] == target:
        return count.get(target)
    elif arr[mid] < target:
        return binarySearch(arr, target, mid + 1, end)
    else:
        return binarySearch(arr, target, start, mid - 1)


for target in candidate:
    print(binarySearch(cards, target, 0, len(cards) - 1), end=" ")
