"""
큰 수의 법칙
: 다양한 수로 이루어진 배열이 있을 때, 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
  단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번 초과하여 더해질 수 없는 것이 특징
  * 반복되는 수열에 대해서 파악 *
"""

# 파이썬 입력 받기
# input() : 입력되는 모 든 것은 문자열!
# map(함수, 리스트) : 리스트의 요소를 지정된 함수로 처리해주는 함수 => 새 리스트 생성
# split(sep='구분자', maxsplit=분할횟수) : 문자열.split(sep, maxsplit) = 문자열을 maxsplit 횟수만큼 sep의 구분자를 기준으로 문자열을 구분하여 잘라서 리스트로 만들기
# sort() : 오름차순 정렬, 리스트만 가능, 리스트 자체를 변경, 리스트.sort()
# sorted() : 오름차순 정렬, 리스트말고도 가능, 리스트를 생성, sorted(리스트)

# * 방법 : 가장 큰 수를 k번 더하고 두 번쨰로 큰 수를 한번 더하는 방법
n, m, k = map(int, input().split())  # [n, m, k] n:배열의 크기, M:더해지는 횟수, K:~번 더할 수 있는지
data = list(map(int, input().split()))  # data = []

data.sort()  # 입력받은 수 정렬하기
first = data[n - 1]  # 가장 큰 수
second = data[n - 2]  # 두번째 큰 수

result = 0

while True:
    # 가장 큰 수를 k번 더하기
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)

# * 방법 : 가장 큰 수가 더해지는 횟수를 구하여 답을 구하는 방법
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]  # 가장 큰 수
second = data[n - 2]  # 두번째 큰 수

count = int(m / (k + 1)) * k  # 가장 큰 수가 등장하는 횟수
count += m % (k + 1)  # 수열 반복 횟수

result = 0
result += (count) * first  # 가장 큰 수 더하기
result += (m - count) * second  # 두 번쨰 큰 수 더하기

print(result)
