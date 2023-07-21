"""
1이 될 때까지 횟수의 최솟값 구하기
* 최대한 많이 나누기 *
"""
# * 내가 푼 방법으로는 최솟값을 구할 수 없음
n, k = map(int, input().split())
result = 0
while n != 1:
    if n % k == 0:
        n = n / k
        result += 1
    else:
        n = n - 1
        result += 1
print(result)

# * 최대한 많이 나누기
n, k = map(int, input().split())
result = 0

while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1

while n > 1:
    n -= 1
    result += 1
print(result)
