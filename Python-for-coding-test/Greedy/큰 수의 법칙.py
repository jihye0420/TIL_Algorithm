# k, m, n = map(int, input().split())  # 반복, 더해지는 횟수, 배열 크기
# data = list(map(int, input().split()))
#
# data.sort()
# first = data[-1]
# second = data[-2]
# print(first)
# print(second)
#
# result = 0
#
# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         result += first
#         m -= 1
#     if m == 0:
#         break
#     result += second
#     m -= 1
#
# print(result)

"""
# 다른 풀이
"""
k, m, n = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[-1]
second = data[-2]

how_many = m // (k + 1)
extra_add = m % (k + 1)

result = 0
# first
result += first * k * how_many
result += first * extra_add
# second
result += second * how_many

print(result)
