# https://school.programmers.co.kr/learn/courses/30/lessons/12943
def solution(num):
    answer = 0
    count = 0
    while num != 1 and count <= 500:
        if num % 2 == 0:  # 짝수라면
            num = num // 2
            count += 1
        else:  # 홀수라면
            num = num * 3 + 1
            count += 1
    return count if count <= 500 else -1


if __name__ == '__main__':
    print(solution(6))
    print(solution(16))
    print(solution(626331))
