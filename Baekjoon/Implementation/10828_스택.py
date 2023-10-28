# https://www.acmicpc.net/problem/10828
# * 실버 4
"""
* 아이디어
- 문자가 바뀌는 시점을 확인
* 알게된 점
- 문자열 슬라이스
"""
import sys

input = sys.stdin.readline
n = int(input())
result = []

for i in range(n):
    speak = input()
    if 'push' in speak:
        result.append(int(speak.split()[-1]))
        continue
    elif 'pop' in speak:
        print(result.pop() if result else -1)
        continue
    elif 'size' in speak:
        print(len(result))
        continue
    elif 'empty' in speak:
        print(0 if result else 1)
        continue
    elif 'top' in speak:
        print(result[-1] if result else -1)
        continue
