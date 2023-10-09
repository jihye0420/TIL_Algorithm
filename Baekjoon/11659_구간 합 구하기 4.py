# https://www.acmicpc.net/problem/11659
n, m = map(int, input().split())
numbers = list(map(int, input().split()))

s = [0]
# s[0] = numbers[0]
# for i in range(1, len(numbers)):
#     s[i] = s[i - 1] + numbers[i]
temp = 0
for i in numbers:
    temp = temp + i
    s.append(temp)

answer = []
for _ in range(m):
    i, j = map(int, input().split())
    answer.append(s[j] - s[i - 1])
# print(answer)

for k in answer:
    print(k)
