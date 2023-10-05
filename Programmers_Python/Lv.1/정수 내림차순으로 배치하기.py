# https://school.programmers.co.kr/learn/courses/30/lessons/12933
def solution(n):
    answer = 0
    # print(type(n))  # int
    answer = list(map(int, str(n)))
    answer.sort(reverse=True)
    for i in range(len(answer)):
        answer[i] = str(answer[i])
    answer = ''.join(answer)
    answer = int(answer)
    return answer


if __name__ == '__main__':
    print(solution(118372))
