# https://school.programmers.co.kr/learn/courses/30/lessons/87389
def solution(n: int):
    answer: int = 0
    i: int = 1
    while True:
        if n % i == 1:
            answer = i
            break
        else:
            i += 1
    return answer


if __name__ == '__main__':
    print(solution(10))
    print(solution(12))
    print(solution(15))

