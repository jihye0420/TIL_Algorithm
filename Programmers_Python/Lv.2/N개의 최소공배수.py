# https://school.programmers.co.kr/learn/courses/30/lessons/12953
from math import gcd


def solution(arr):
    answer = arr[0]
    for i in arr:
        answer = answer * i // gcd(answer, i)
    return answer


if __name__ == '__main__':
    print(solution([2, 6, 8, 14]))
