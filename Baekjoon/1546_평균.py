# https://www.acmicpc.net/problem/1546
n = int(input())
score = list(map(int, input().split()))

m = max(score)

answer = 0
for i in score:
    answer += i / m * 100

print(answer / len(score))
