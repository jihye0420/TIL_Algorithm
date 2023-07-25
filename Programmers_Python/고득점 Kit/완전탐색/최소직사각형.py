# todo: 다시 풀어보기
# 아이디어: 가장 큰 값은 모두 가로로, 작은 값은 모두 세로로 => 각 max 값을 곱하기
# https://school.programmers.co.kr/learn/courses/30/lessons/86491
# def solution(sizes):
#     answer = 0
#     w = [0] * len(sizes)
#     h = [0] * len(sizes)
#     for i in range(len(sizes)):
#         # sizes[i]
#         # print(sizes[i][0], sizes[i][1])
#         if sizes[i][0] >= sizes[i][1]:
#             w[i] = sizes[i][0]
#             h[i] = sizes[i][1]
#         else:
#             w[i] = sizes[i][1]
#             h[i] = sizes[i][0]
#     # print(w)
#     # print(h)
#     answer = max(w) * max(h)
#     return answer


def solution(sizes):
    answer = 0
    w = [0] * len(sizes)
    h = [0] * len(sizes)
    for i in range(len(sizes)):
        # sizes[i]
        # print(sizes[i][0], sizes[i][1])
        if sizes[i][0] >= sizes[i][1]:
            w[i] = sizes[i][0]
            h[i] = sizes[i][1]
        else:
            w[i] = sizes[i][1]
            h[i] = sizes[i][0]
    # print(w)
    # print(h)
    answer = max(w) * max(h)
    return answer

if __name__ == '__main__':
    print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
    print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
    print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))
