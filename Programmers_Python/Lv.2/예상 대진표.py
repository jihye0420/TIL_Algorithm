# https://school.programmers.co.kr/learn/courses/30/lessons/12985

def solution(n: int, a: int, b: int) -> int:
    answer = 0
    # 언제까지? => a와 b가 만났을 때까지 answer +=1
    while n//2 != 1:

        # 2개의 리스트 씩
        1 2 | 3 4 | 5 6 | 7 8 | 9 10 | 11 12  | 13 14
         1  |  4  |  5  | 7  | 10   | 11    | 13
            4     |    7     | 10  | 13
                4? 10? # 둘중 하나
        answer += 1
        # 하나씩 줄여나가기

    return answer


if __name__ == '__main__':
    print(solution(8, 4, 7))
