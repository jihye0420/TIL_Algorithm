# https://www.acmicpc.net/problem/2941
# * 실버 5
"""
* 아이디어
- split
- replace
* 알게된 점
- 문자열 함수
    - split('구분자') : 문자열 나누기
    - replace() : 문자열 바꾸기
"""
data = input()

croatia_alpabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for c in croatia_alpabet:
    data = data.replace(c, '*')
print(len(data))
