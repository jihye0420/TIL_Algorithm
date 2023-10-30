# 입력
# 10
# 6 3 2 10 10 10 -10 -10 7 3
# 8
# 10 9 -5 2 3 4 5 -10
"""
나만의 풀이 => 시간초과
1. 리스트 => 시간초과
2. 딕셔너리로 풀어보기
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
이분 탐색
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
