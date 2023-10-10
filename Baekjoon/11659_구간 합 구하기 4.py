# https://www.acmicpc.net/problem/11659
n, m = map(int, input().split())
numbers = list(map(int, input().split()))

s = [0]  # ! index 1부터 값이 채워짐
temp = 0
for i in numbers:
    temp = temp + i
    s.append(temp)
# print(s)

answer = []
for _ in range(m):
    i, j = map(int, input().split())
    print(s[j] - s[i - 1])
    # answer.append(s[j] - s[i - 1])

# for k in answer:
#     print(k)
