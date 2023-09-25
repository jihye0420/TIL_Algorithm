# https://school.programmers.co.kr/learn/courses/30/lessons/12985
def solution(n: int, a: int, b: int) -> int:
    answer = 0
    # 언제까지? => a와 b가 만났을 때까지 answer +=1
    while a != b:
        a, b = (a + 1) // 2, (b + 1) // 2
        answer += 1
    return answer


if __name__ == '__main__':
    print(solution(8, 4, 7))
