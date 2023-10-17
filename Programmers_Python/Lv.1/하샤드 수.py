# https://school.programmers.co.kr/learn/courses/30/lessons/12947
def solution(x):
    answer = True
    tmp_x = list(map(int, str(x)))
    temp = sum(tmp_x)
    print(temp)
    if x % temp == 0:
        answer = True
    else:
        answer = False
    return answer


if __name__ == '__main__':
    print(solution(10))
    print(solution(12))
    print(solution(11))
    print(solution(13))
