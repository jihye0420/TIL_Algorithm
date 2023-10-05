# https://school.programmers.co.kr/learn/courses/30/lessons/12954
def solution(x, n):
    answer = []
    # x부터 x씩 증가하는 숫자 n개 리스트 리턴
    tmp = x
    for i in range(n):
        answer.append(tmp)
        tmp = tmp + x
    return answer


if __name__ == '__main__':
    print(solution(2, 5))
    print(solution(4, 3))
    print(solution(-4, 2))
