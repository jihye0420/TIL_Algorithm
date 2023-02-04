# https://school.programmers.co.kr/learn/courses/30/lessons/77484
def solution(lottos, win_nums: list):
    answer = [0, 0]
    win = 0  # 맞힌 개수를 셈
    temp = 0  # 0의 개수를 셈
    for l in lottos:
        if l in win_nums:
            win_nums.remove(l)
            win += 1
        if l == 0:
            temp += 1
    answer[1] = 6 if (7 - win == 6) or (7 - win == 7) else 7 - win
    if len(win_nums) >= temp:
        win += temp
    else:
        win += len(win_nums)
    answer[0] = 6 if (7 - win == 6) or (7 - win == 7) else 7 - win
    return answer


if __name__ == '__main__':
    # print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
    print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
