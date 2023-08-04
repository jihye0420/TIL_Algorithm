# https://school.programmers.co.kr/learn/courses/30/lessons/84512
# * 배운점 : product (순열(원소 중복 허용))
from itertools import product


def solution(word):
    answer = 0
    alpabet = ['A', 'E', 'I', 'O', 'U']
    words = []
    for i in range(1, len(alpabet) + 1):
        for j in product(alpabet, repeat=i):
            words.append(''.join(list(j)))
    words.sort()
    # print(words)
    return words.index(word) + 1


if __name__ == '__main__':
    print(solution("AAAAE"))
    print(solution("AAAE"))
    print(solution("I"))
    print(solution("EIO"))
