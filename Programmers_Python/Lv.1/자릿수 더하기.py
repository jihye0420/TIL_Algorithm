# https://school.programmers.co.kr/learn/courses/30/lessons/12931
def solution(n: int):
    answer: int = 0
    temp: list[str] = list(map(int, str(n)))
    for i in temp:
        answer += int(i)
    return answer


if __name__ == '__main__':
    print(solution(123))
