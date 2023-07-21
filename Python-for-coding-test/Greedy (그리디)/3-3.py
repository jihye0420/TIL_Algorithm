"""
숫자 카드 게임
: 여러개의 숫자 카드 중 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임
  * 각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰 수를 찾는 것 *
"""
# iterable : dict, set, list, tuple

# * 방법 1) min()함수를 이용한 방법 예시
n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)
print(result)
