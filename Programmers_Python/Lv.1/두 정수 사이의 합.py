# https://school.programmers.co.kr/learn/courses/30/lessons/12912?language=python3
def solution(a: int, b: int) -> int:
    answer: int = 0
    i: int = a if a < b else b
    temp: int = b if a < b else a
    while True:
        if i == temp:
            answer += i
            break
        answer += i
        i += 1
    return answer


if __name__ == '__main__':
    print(solution(3, 5))
