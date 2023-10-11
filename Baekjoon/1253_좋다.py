# https://www.acmicpc.net/problem/1253
"""
# 나만의 풀이 => 출력 결과는 맞지만, 백준 채점에서 틀림
"""
n = int(input())
data = list(map(int, input().split()))
data.sort()

count = 0

# for i in range(n):
#     start = 0
#     end = n - 1
#     while start < end:
#         if data[start] + data[end] < data[i]:
#             start += 1
#         elif data[start] + data[end] > data[i]:
#             end -= 1
#         elif data[start] + data[end] == data[i]:
# ! 아래에 서로 같은 수인지 확인이 필요함!
#             count += 1
#             break
# print(count)

"""
# 책의 풀이 => 투 포인터 알고리즘
"""
for k in range(n):
    find = data[k]
    i = 0
    j = n - 1
    while i < j:  # 투 포인터 알고리즘
        if data[i] + data[j] == find:  # find는 서로 다른 두 수의 합이어야 함을 체크!
            if i != k and j != k:  # 서로 다른 두 수
                count += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif data[i] + data[j] < find:
            i += 1
        else:
            j -= 1
print(count)
