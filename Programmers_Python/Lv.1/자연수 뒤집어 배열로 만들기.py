# https://school.programmers.co.kr/learn/courses/30/lessons/12932
def solution(n):
    answer = []
    # * 기존 코드
    # answer = list(str(n))
    # for i in range(len(answer)):
    #     answer[i] = int(answer[i])

    # * 개선된 코드
    answer = list(map(int, str(n)))
    return answer[::-1]


if __name__ == '__main__':
    print(solution(12345))
