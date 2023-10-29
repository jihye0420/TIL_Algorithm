# https://www.acmicpc.net/problem/9012
# * 실버 4
"""
* 아이디어
- 스택 이용
* 알게된 점
"""


def check(data):
    stack = []
    ok = True
    for i in data:
        if not stack and i == ')':
            ok = False
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
    if stack or ok == False:
        print('NO')
    else:
        print('YES')


n = int(input())
for i in range(n):
    data = input()
    check(data)
