# https://www.acmicpc.net/problem/1931
# * 실버 1
"""
* 아이디어
- 경우의 수를 적게, 예시로 파악하기 => 전체를 시작시간의 오름차순으로 정렬을 한 뒤, 정렬된 리스트를 다시 끝나는 시간으로 오름차순 정렬
* 알게된 점
- 내장함수 (정렬)
    - sorted(정렬할 데이터, key 파라미터, reverse 파라미터) : key를 기준으로 오름차순 정렬 / reverse=True일 때는 내림차순 정렬
"""

N = int(input())
time = []

for _ in range(N):
    start, end = map(int, input().split())
    time.append([start, end])

time = sorted(time, key=lambda a: a[0])  # 시작 시간을 기준으로 오름차순
# print(time)
time = sorted(time, key=lambda a: a[1])  # 끝나는 시간을 기준으로 다시 오름차순
# print(time)

last = 0  # 회의의 마지막 시간을 저장할 변수
conut = 0  # 회의 개수를 저장할 변수

for i, j in time:
    if i >= last:  # 시작시간이 회의의 마지막 시간보다 크거나 같을경우
        conut += 1
        last = j

print(conut)
