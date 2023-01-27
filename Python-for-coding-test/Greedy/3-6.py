# * 3-5.py와 다른 방법
n, k = map(int, input().split())
result = 0

while True:
    # n == k 가 될때까지 나누기
    target = (n // k) * k
    result += (n - target)
    n = target
    if n < k:
        break
    n //= k
    result += 1

result += (n - 1)  # n은 아직 1이 아니므로, 최종 연산 횟수에 1이 되기 위해 뺴야하는 횟수를 구하는 과정
print(result)
