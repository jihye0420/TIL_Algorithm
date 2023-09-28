# * 참고 : https://seongonion.tistory.com/40
n = int(input())

# d[i]는 숫자 i가 1이 되는데 걸리는 최소한의 연산 횟수
d = [0] * 30001

for i in range(2, n + 1):
    d[i] = d[i - 1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[n])
