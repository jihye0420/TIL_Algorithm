# https://school.programmers.co.kr/learn/courses/30/lessons/12944
def solution(arr):
    answer = 0
    answer = sum(arr) / len(arr)
    return answer


if __name__ == '__main__':
    print(solution([1, 2, 3, 4]))
    print(solution([5, 5]))
