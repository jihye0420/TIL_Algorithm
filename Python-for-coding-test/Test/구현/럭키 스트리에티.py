# https://www.acmicpc.net/problem/18406
N = list(map(int, input()))
half = len(N) // 2
temp = 0
temp2 = 0
for i in range(half):
    temp += N[i]
for i in range(half, len(N)):
    temp2 += N[i]

if temp == temp2:
    print("LUCKY")
else:
    print("READY")
