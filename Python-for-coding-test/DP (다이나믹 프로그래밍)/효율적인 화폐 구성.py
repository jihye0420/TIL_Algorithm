# * 나의 풀이 => 불확실함(동전의 단위가 배수가 아니므로)
# n, m = map(int, input().split())
# data = []
# for i in range(n):
#     data.append(int(input()))
#
#
# def solution(n, m, data):
#     answer = 0
#     data.sort(reverse=True)
#     for i in data:
#         if m % i == 0:
#             answer += m // i
#     if answer == 0:
#         answer = -1
#     return answer
#
#
# print(solution(n, m, data))

# * 책의 풀이
# 참고: https://hgk5722.tistory.com/12
n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m + 1)

d[0] = 0
for i in range(n):  # i : 각각의 화폐 단위
    for j in range(array[i], m + 1):  # j : 각각의 금액
        if d[j - array[i]] != 10001:  # (i-k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
