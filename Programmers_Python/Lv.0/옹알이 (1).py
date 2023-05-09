# https://school.programmers.co.kr/learn/courses/30/lessons/120956
from itertools import permutations


# for i in permutations([], 4):
#     print(i)

def solution(babbling):
    answer = 0
    possible_lang = ['aya', 'ye', 'woo', 'ma']
    temp_lang = []
    for i in range(1, len(possible_lang) + 1):
        for j in permutations(possible_lang, i):
            temp_lang.append(''.join(j))
    print(temp_lang)

    for i in babbling:
        if i in temp_lang:
            answer += 1

    return answer


if __name__ == '__main__':
    print(solution(["aya", "yee", "u", "maa", "wyeoo"]))
