n = int(input())
p = list(map(int, input().split()))

p.sort()

answer = 0
for i, v in enumerate(p):
    for ii in range(i + 1):
        answer += p[ii]

print(answer)
