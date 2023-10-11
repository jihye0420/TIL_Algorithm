# https://www.acmicpc.net/problem/1940
"""
# 나만의 풀이 => 시간 초과로 실패
"""
# n = int(input())
# m = int(input())
# numbers = list(map(int, input().split()))
#
# count = 0
# temp = 0
#
# for i in range(n):  # 0 1 2 3 4 5
#     for j in range(i + 1, n):  # i+1, ...
#         sum_num = numbers[i] + numbers[j]
#         if sum_num == m:
#             count += 1
#         else:
#             continue
#
# print(count)

"""
# 책의 풀이 => 경우의 수를 나누고 2가지 포인터를 활용
"""
n = int(input())
m = int(input())
a = list(map(int, input().split()))
a.sort()
i = 0
j = n - 1
count = 0
while i < j:
    if a[i] + a[j] > m:
        j -= 1
    elif a[i] + a[j] < m:
        i += 1
    else:
        count += 1
        i += 1
        j -= 1

print(count)
