# https://www.acmicpc.net/problem/2941
# * 실버 5
"""
* 아이디어
- split
* 알게된 점
- split
"""
data = str(input())

croatia_alpabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for c in croatia_alpabet:
    if c in data:
        data = data.split(c)
        print(data)
print(len(data)+1)
