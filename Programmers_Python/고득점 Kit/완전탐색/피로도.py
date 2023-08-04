# https://school.programmers.co.kr/learn/courses/30/lessons/87946
# * 배운점 :
from itertools import permutations


def solution(k, dungeons):
    temp_list = list(permutations(dungeons, len(dungeons)))
    answer = [0] * len(temp_list)
    a = [k] * len(temp_list)
    # print(temp_list)
    # 순서 상관없이 확인
    for i in range(len(temp_list)):
        # print(temp_list[i])
        for j in temp_list[i]:
            # print(j)
            if a[i] >= j[0]:
                a[i] -= j[1]
                answer[i] += 1
            else:
                continue
    return max(answer)


if __name__ == '__main__':
    print(solution(80, [[80, 20], [50, 40], [30, 10]]))
