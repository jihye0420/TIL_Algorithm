# https://school.programmers.co.kr/learn/courses/30/lessons/42576?language=python3
from collections import Counter


def solution(participant: list, completion: list) -> str:
    # answer = ''
    # 차집합을 이용시, 동명이인에 대해서 처리가 어려움
    # not_completion = list(set(participant) - set(completion))
    # answer = not_completion[0]

    counter = Counter(participant)
    value = list(counter.values())
    for c in completion:
        counter[c] -= 1
    answer= [k for k, v in counter.items() if v == 1]
    return answer[0]


if __name__ == '__main__':
    print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
    print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
