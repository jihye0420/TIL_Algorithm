# https://www.acmicpc.net/problem/10773
# * 실버 4
"""
* 아이디어
- 스택 이용
* 알게된 점
"""
stack = []
n = int(input())
for i in range(n):
    num = int(input())
    if num == 0:
        if stack:
            stack.pop()
    else:
        stack.append(num)
print(sum(stack))
