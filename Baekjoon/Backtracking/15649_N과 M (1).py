# https://www.acmicpc.net/problem/15649
# * 실버 3
"""
1. 아이디어
- 1 ~ N 중에 하나를 선택한 뒤 => for문
- 다음 1부터 N부터 선택할 떄 이미 선택한 값이 아닌 경우 선택 => 방문 여부 확인
- M개를 선택할 경우 프린트  => 종료 조건 확인
2. 시간복잡도
- N ^ N : 중복이 가능, N = 8 까지 가능
- N! : 중복이 불가, N = 10 까지 가능
3. 자료구조
- 백트래킹
- 방문 여부 확인 배열 : bool[]
- 선택한 값 입력 배열 : int[]
"""

"""
1. 아이디어
- 백트래킹 재귀함수 안에서, for 돌면서 숫자 선택(이때 방문여부 확인)
- 재귀함수에서 M개를 선택할경우 print

2. 시간복잡도
- N! > 가능

3. 자료구조
- 결과값 저장 int[]
- 방문여부 체크 bool[]

# todo: 이해+암기...
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
rs = []
chk = [False] * (n + 1)


def recur(num):
    if num == m:
        print(' '.join(map(str, rs)))
        return
    for i in range(1, n + 1):
        if chk[i] == False:
            chk[i] = True
            rs.append(i)
            recur(num + 1)
            chk[i] = False
            rs.pop()


recur(0)
