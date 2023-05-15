# https://school.programmers.co.kr/learn/courses/30/lessons/181893
def solution(arr: list, query: list) -> list:
    answer = []
    for i in query:
        if i % 2 == 0:
            arr = arr[0:i + 1]
        else:
            arr = arr[i:]
    return arr


if __name__ == '__main__':
    print(solution([0, 1, 2, 3, 4, 5], [4, 1, 2]))
