# https://school.programmers.co.kr/learn/courses/30/lessons/12934
def solution(n):
    # n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴
    tmp = 0
    answer = False
    # 반복문으로 해결
    while tmp <= n:
        if tmp * tmp == n:
            answer = True
            break
        else:
            tmp += 1
    if answer:
        return (tmp + 1) * (tmp + 1)
    else:
        return -1


if __name__ == '__main__':
    print(solution(121))
    print(solution(3))
