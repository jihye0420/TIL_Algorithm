# https://school.programmers.co.kr/learn/courses/30/lessons/42840
# * 배운점 : i % n , enumerate
def solution(answers):
    answer = []
    person = [0] * 3  # 3명의 수포자가 맞춘 개수를 넣을 리스트
    a1 = [1, 2, 3, 4, 5]  # 1번째 수포자의 답을 넣은 리스트
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]  # 2번째 수포자의 답을 넣은 리스트
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 3번째 수포자의 답을 넣은 리스트

    # 맞춘 개수를 확인하는 코드
    for i in range(len(answers)):
        # 1번째 수포자는 5개의 답이 반복되므로 [i%5] 해줌
        if answers[i] == a1[i % 5]:
            person[0] += 1
        # 2번째 수포자는 8개의 답이 반복되므로 [i%5] 해줌
        if answers[i] == a2[i % 8]:
            person[1] += 1
        # 3번째 수포자는 10개의 답이 반복되므로 [i%5] 해줌
        if answers[i] == a3[i % 10]:
            person[2] += 1

    winner = max(person)  # 가장 많이 맞춘 사람의 개수를 넣는 변수

    # 가장 많이 맞춘 사람을 넣는 코드 (공동 1등이 나올 수 있으므로)
    for i in range(len(person)):
        if person[i] == winner:
            answer.append(i + 1)
    return answer


"""
* 다른 풀이
"""


def solution(answers):
    p = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(p)

    for q, a in enumerate(answers):
        for i, v in enumerate(p):
            if a == v[q % len(v)]:
                s[i] += 1
    return [i + 1 for i, v in enumerate(s) if v == max(s)]


if __name__ == '__main__':
    print(solution([1, 2, 3, 4, 5]))
    print(solution([1, 3, 2, 4, 2]))
