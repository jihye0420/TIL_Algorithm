# https://www.acmicpc.net/problem/11399
# * 실버 4
"""
* 아이디어
* 알게된 점
- enumerate() : 순서가 있는 데이터(리스트, 튜플, 문자열)를 입력 받아 인덱스 값을 포함하는 enumerate 객체 리턴
"""

n = int(input())
p = list(map(int, input().split()))

p.sort()

answer = 0
for i, v in enumerate(p):
    for ii in range(i + 1):
        answer += p[ii]

print(answer)
