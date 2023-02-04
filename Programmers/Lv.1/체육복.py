# https://school.programmers.co.kr/learn/courses/30/lessons/42862
# todo: 아래 풀이는 test 케이스 중 80만 정답 (이유: 도난, 여분 학생이 동일할 시, 빌려줄 수 없는 케이스 고려 안한 것)
# def solution(n, lost, reserve):
#     # n: 전체 학생의 수
#     # lost: 도난당한 학생들의 번호
#     # reserve: 여분 학생들의 번호
#
#     for i in range(len(reserve)):
#         print(lost)
#         tmp1 = reserve[i] - 1
#         tmp2 = reserve[i] + 1
#         tmp3 = reserve[i]
#         if tmp1 in lost and tmp3 not in lost:
#             lost.remove(tmp1)
#             continue
#         elif tmp2 in lost and tmp3 not in lost:
#             lost.remove(tmp2)
#             continue
#         elif tmp3 in lost:
#             lost.remove(tmp3)
#             continue
#
#     n -= len(lost)
#
#     answer = n
#     return answer


def solution(n, lost, reserve):
    # n: 전체 학생의 수
    # lost: 도난당한 학생들의 번호
    # reserve: 여분 학생들의 번호
    tmp_lost = list(set(lost) - set(reserve))
    tmp_reserve = list(set(reserve) - set(lost))
    for i in range(len(tmp_reserve)):
        # print(lost)
        tmp1 = tmp_reserve[i] - 1
        tmp2 = tmp_reserve[i] + 1
        tmp3 = tmp_reserve[i]
        if tmp1 in tmp_lost and tmp3 not in tmp_lost:
            tmp_lost.remove(tmp1)
            continue
        elif tmp2 in tmp_lost and tmp3 not in tmp_lost:
            tmp_lost.remove(tmp2)
            continue
        elif tmp3 in tmp_lost:
            tmp_lost.remove(tmp3)
            continue

    n -= len(tmp_lost)

    answer = n
    return answer


if __name__ == '__main__':
    print(solution(5, [2, 5, 4, 1], [2, 3, 4]))
    # print(solution(5, [2, 4], [3]))
    # print(solution(3, [3, 2], [3]))
    # print(solution(2, [2], [1]))
