# https://school.programmers.co.kr/learn/courses/30/lessons/76501
def solution(absolutes, signs):
    answer = 0

    for a, s in zip(absolutes, signs):
        if s == True:
            answer += a
        else:
            answer -= a

    return answer


if __name__ == '__main__':
    print(solution([4, 7, 12], [True, False, True]))
    print(solution([1, 2, 3], [False, False, True]))
