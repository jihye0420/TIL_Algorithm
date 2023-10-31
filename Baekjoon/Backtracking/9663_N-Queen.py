# https://www.acmicpc.net/problem/9663
"""
1. 아이디어
2. 시간복잡도
3. 자료구조
"""
import sys

sys.setrecursionlimit(10 ** 4)

"""
# Backtrack 함수의 작동 방식
(1) 현재 Row가 보드판 사이즈인 n보다 크면 가능한 방법 한 가지를 찾았다 생각하고 1을 리턴한다.
(2) 지역변수 solutions를 0으로 초기화. solutions는 현재 보드 상태에서 가능한 해결방법의 수를 나타냄
(3) 현재 Row의 모든 Columns에 대해 순회를 돌면서 퀸을 놓을 수 있는지 여부를 살펴본다.
    - 현재 칸의 대각선, anti-대각선을 계산한다.
    - 현재 칸의 열, 대각선, anti-대각선에 위치한 퀸이 있으면 퀸을 놓을 수 없으므로 다음 컬럼으로 넘어간다.
    - 현재 칸에 퀸을 놓을 수 있다면 3개의 set(cols, diagonals, anti_diagonals)를 업데이트 하고, row+1 파라미터로 함수를 호출한다.
(4) 탐색을 완료하면 되돌아가면서(backtrack) 퀸을 회수한다. 즉, set에 추가한 값들을 제거한다.
"""


def n_queens(n):
    # diagonals: 대각선으로 놓인 퀸들의 위치 정보 (row - col)
    # anti_diagonals: 역방향 대각선으로 놓인 퀸들의 정보 (row + col)
    # cols: 배열의 인덱스 = Row. 각 행의 몇 번째 컬럼에 퀸이 위치하는지에 대한 정보
    def backtrack(row, diagonals, anti_diagonals, cols):
        # Base Case: 현재 Row가 보드판 사이즈인 n이 되면 가능한 방법 한 가지를 찾았다 생각하고 1을 리턴한다.
        if row == n:
            return 1

        # 지역변수 solutions의 값을 0으로 초기화. solutions는 현재 보드 상태에서 가능한 해결방법의 수를 나타냄
        solutions = 0

        for col in range(n):
            # 오른쪽 아래로 내려가는 대각선은 같은 대각선에 있는 칸들의 row-col 값이 같다.
            curr_diagonal = row - col
            # 오른쪽 위로 올라가는 대각선은 같은 대각선에 있는 칸들의 row+col 값이 같다.
            curr_anti_diagonal = row + col

            # 만약 현재 칸의 열, 대각선, anti-대각선에 놓인 퀸이 있으면 퀸을 놓을 수 없으므로 다음 컬럼으로 넘어간다.
            if (col in cols
                    or curr_diagonal in diagonals
                    or curr_anti_diagonal in anti_diagonals):
                continue

            # 현재 칸에 퀸을 놓을 수 있다면 3개의 set(cols, diagonals, anti_diagonals)를 업데이트
            cols.add(col)
            diagonals.add(curr_diagonal)
            anti_diagonals.add(curr_anti_diagonal)

            # 보드의 상태가 업데이트된 상태로 다음 행으로 넘어감
            solutions += backtrack(row + 1, diagonals, anti_diagonals, cols)

            # "Remove" the queen from the board since we have already
            # explored all valid paths using the above function call
            # 탐색을 완료하면 되돌아가면서(backtrack) 퀸을 회수한다. 즉, set에 추가한 값들을 제거한다.
            cols.remove(col)
            diagonals.remove(curr_diagonal)
            anti_diagonals.remove(curr_anti_diagonal)

        return solutions

    # 처음 재귀함수를 호출하는 지점
    return backtrack(0, set(), set(), set())


N = int(sys.stdin.readline())
print(n_queens(N))
