# https://school.programmers.co.kr/learn/courses/30/lessons/120583
def solution(array: list, n: int):
    answer = 0
    for i in array:
        if n == i:
            answer += 1
    return answer


if __name__ == '__main__':
    print(solution([1, 1, 2, 3, 4, 5], 1))
