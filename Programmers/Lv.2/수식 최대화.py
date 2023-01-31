# todo: 중요중요 가다시 풀어보기
# https://school.programmers.co.kr/learn/courses/30/lessons/67257

from itertools import permutations


# 수식 기준 자르기
# 나올 수 있는 순열 먼저 뽑기 -> 계산 한 수 중 가장 큰 값을 answer로 !
# enumerate() : index, 값을 리턴(value)
def solution(expression):
    operators = ["*", "+", "-"]
    answer = []
    for oper in permutations(operators, 3):  # 순열
        print(oper)
        a = oper[0]
        b = oper[1]
        tmp_list = []
        for i in expression.split(a):
            tmp = [f"({j})" for j in i.split(b)]
            print(tmp)
            tmp_list.append(f"({b.join(tmp)})")
            answer.append(abs(eval(a.join(tmp_list))))
    return max(answer)


if __name__ == '__main__':
    print(solution("100-200*300-500+20"))
    # [100, -, 200, *, 300, -, 500, +, 20]
