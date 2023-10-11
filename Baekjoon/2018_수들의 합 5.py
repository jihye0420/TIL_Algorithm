# https://www.acmicpc.net/problem/2018
"""
# 나만의 풀이 => 시간 초과로 실패
"""
# n = int(input())
#
# answer = 0
# for i in range(1, n):
#     temp = i
#     sum_temp = 0
#     while True:
#         if sum_temp > n:
#             break
#         if sum_temp == n:
#             answer += 1
#         sum_temp += temp
#         temp += 1
#
# print(answer + 1)  # 자기 자신의 숫자

"""
# 책의 풀이 => 경우의 수를 나누고 2가지 포인터를 활용
"""
n = int(input())
count = 1
start_index = 1
end_index = 1
sum = 1

while end_index != n:
    if sum == n:
        count += 1
        end_index += 1
        sum += end_index
    elif sum > n:
        sum -= start_index
        start_index += 1
    else:
        end_index += 1
        sum += end_index

print(count)
