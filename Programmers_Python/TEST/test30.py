# def solution(board, k, ax, ay, bx, by):
#     answer = -2
#     return answer
# if __name__ == '__main__':
#     print(solution([[1, 2, 0, 0], [1, 0, 2, 0], [1, 0, 0, 0], [1, 0, 0, 1]], 2, 1, 1, 2, 2))


def main():
    board = [[1, 2, 0, 0], [1, 0, 2, 0], [1, 0, 0, 0], [1, 0, 0, 1]]
    k = 2
    Ax, Ay = 1, 1
    Bx, By = 2, 2
    # board = [[0, 0, 1, 0, 0, 0], [0, 2, 0, 0, 0, 1], [0, 0, 2, 1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 0]]
    # k = 2
    # Ax, Ay = 1, 2
    # Bx, By = 0, 5

    print(solution(board, k, Ax, Ay, Bx, By))


def solution(board, K, Ax, Ay, Bx, By):
    N = len(board)

    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                bomb_check(board, i, j, K)

    # Your additional logic and calculations can go here
    answer = 0
    print("board: ", board)
    return answer


def bomb_check(board, x, y, k):
    # up, down, left, right = True, True, True, True
    n = len(board)
    print(board)

    # for i in range(n):
    #     for j in range(i):
    #         print(i, " : ", j)

    # 상하좌우 거리 다 표시해서 벗어난 경로가 아니면 표시
    for i in range(k + 1):
        # up
        nx = x + i
        ny = x + i
        # down
        # left
        # right
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            break
        [nx


if __name__ == "__main__":
    main()
