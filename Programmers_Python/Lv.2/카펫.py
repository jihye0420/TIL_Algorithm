# https://school.programmers.co.kr/learn/courses/30/lessons/42842
def solution(brown, yellow):
    answer = []
    # total = brown + yellow
    for i in range(1, yellow + 1):
        if (yellow % i) == 0:
            yellow_row = yellow // i
            yellow_col = i
            if (2 * (yellow_col + yellow_row) + 4) == brown:
                return [yellow_row + 2, yellow_col + 2]


if __name__ == '__main__':
    print(solution(10, 2))
