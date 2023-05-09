# https://school.programmers.co.kr/learn/courses/30/lessons/12919
def solution(seoul):
    w = seoul.index('Kim')
    answer = '김서방은 ' + str(w) + '에 있다'
    return answer


if __name__ == '__main__':
    print(solution(["Jane", "Kim"]))
