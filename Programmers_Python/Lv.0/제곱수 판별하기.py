# todo: 다른 방법도 찾아보기
# https://school.programmers.co.kr/learn/courses/30/lessons/120909
def solution(n):
    answer = 2
    x = 1
    while x <= 1000000:
        if n == x * x:
            answer = 1
            break
        else:
            x += 1
    return answer


if __name__ == '__main__':
    print(solution(144))
    print(solution(976))
